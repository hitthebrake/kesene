import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required

from authorization.models import CustomUser, Department, Position, Organization


# Create your views here.


def can_create_user(user):
    return user.can_create_user or user.is_superuser

def login_view(request):
    if request.user.is_authenticated:
        return redirect('monitoring:index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active and not user.is_deleted:
                login(request, user)
                return redirect('monitoring:index')
            messages.error(request, 'Пользователь отключен либо удален')
        else:
            messages.error(request, 'Недействительная электронная почта или неправильный пароль')
    return render(request, 'authorization/login.html')

@login_required(login_url='authorization:login')
def logout_view(request):
    logout(request)
    return render(request, 'authorization/sign-out.html')


@user_passes_test(can_create_user, login_url='authorization:login')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2:
            messages.error(request, "Пароли не совпадают*")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Электронная почта уже используется*")
        else:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password1,
                phone=phone,
                first_name=first_name,
                last_name=last_name,
                can_add_data='add_data' in request.POST,
                can_create_user='create_user' in request.POST,
                can_add_threshold='add_threshold' in request.POST
            )
            messages.success(request, 'Пользователь успешно создан')

    users = CustomUser.objects.values('first_name', 'last_name', 'email', 'phone', 'can_add_data', 'can_add_threshold', 'can_create_user')
    return render(request, 'authorization/signup.html', {'users': users})


def forgot_password(request):
    return render(request, 'authorization/forgot-password.html')


@login_required(login_url='authorization:login')
def add_organization(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        district = request.POST.get('district')
        street = request.POST.get('street')
        building_number = request.POST.get('building_number')
        contact_phone = request.POST.get('contact_phone')
        email = request.POST.get('email')

        departments_name = set(request.POST.getlist('departments_name'))
        positions_name = set(request.POST.getlist('positions_name'))

        if not Organization.objects.filter(name=name).exists():
            organization = Organization(
                name=name,
                city=city,
                district=district,
                street=street,
                building_number=building_number,
                contact_phone=contact_phone,
                contact_email=email,
            )
            organization.save()

        organization = Organization.objects.get(name=name)

        existing_departments = organization.departments.filter(name__in=departments_name).values_list('name', flat=True)
        existing_positions = organization.positions.filter(name__in=positions_name)
        for department_name in departments_name:
            if department_name not in existing_departments:
                department = Department(
                    name=department_name,
                    organization=organization,
                )
                department.save()
        for position_name in positions_name:
            if position_name not in existing_positions:
                position = Position(
                    name=position_name,
                    organization=organization,
                )
                position.save()

        return redirect('authorization:add_organization')

    return render(request, 'authorization/add-organization.html')


@login_required(login_url='authorization:login')
def add_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        patronym = request.POST.get('patronym')
        department_id = request.POST.get('organization_department')
        position_id = request.POST.get('organization_position')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        permissions = request.POST.getlist('permissions')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Пароли не совпадают*")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Электронная почта уже используется*")
        else:
            user = CustomUser.objects.create_user(
                username=email,
                patronym=patronym,
                email=email,
                password=password,
                phone=phone_number,
                first_name=first_name,
                last_name=last_name,
                can_add_data='manual_input' in permissions,
                can_add_threshold='threshold' in permissions,
                is_admin='admin' in permissions,
                position_id=position_id,
                department_id=department_id,
            )
            messages.success(request, 'Пользователь успешно создан')
            return redirect('authorization:add_user')

    organizations = Organization.objects.all().values('name', 'id')
    return render(request, 'authorization/add_user.html', {'organizations': organizations})


@login_required(login_url='authorization:login')
def deleted_users_view(request):
    users = CustomUser.objects.select_related('department', 'position').filter(is_deleted=True) \
        .values('department__name', 'position__name', 'organization__name',
                'first_name', 'last_name', 'phone', 'email', 'patronym', 'id',
                )
    return render(request, 'authorization/deleted.html', {'users': users})


@login_required(login_url='authorization:login')
def off_users_view(request):
    users = CustomUser.objects.select_related('department', 'position').filter(is_active=False, is_deleted=False) \
        .values('department__name', 'position__name', 'organization__name',
                'first_name', 'last_name', 'phone', 'email', 'patronym', 'id',
                )
    return render(request, 'authorization/off.html', {'users': users})


@login_required(login_url='authorization:login')
def users_view(request):
    users = CustomUser.objects.select_related('department', 'position').filter(is_active=True, is_deleted=False) \
        .values('department__name', 'position__name', 'organization__name',
                'first_name', 'last_name', 'phone', 'email', 'patronym', 'id', 'created_at',
                'is_admin', 'can_add_data', 'can_add_settings'
                )
    organizations = Organization.objects.all().values('name', 'id')
    return render(request, 'authorization/users.html', {'users': users, 'organizations': organizations})


def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_deleted = True
    user.save()
    return redirect('authorization:users')


def user_recover(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_deleted = False
    user.is_active = True
    user.save()
    return redirect('authorization:users')


def user_disable(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect('authorization:users')


def user_enable(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('authorization:users')


@login_required(login_url='authorization:login')
def get_organization_details(request):
    organization_id = request.GET.get('organization')

    departments = list(Department.objects.filter(organization_id=organization_id).values('name', 'id'))
    positions = list(Position.objects.filter(organization_id=organization_id).values('name', 'id'))

    return JsonResponse({
        "departments": departments,
        "positions": positions
    })


@login_required(login_url='authorization:login')
def edit_organization(request, organization_id):
    try:
        organization = Organization.objects.get(id=organization_id)
        departments = list(organization.departments.values_list('name', flat=True))
        positions = list(organization.positions.values_list('name', flat=True))
    except Organization.DoesNotExist:
        organization = None
        departments = None
        positions = None

    if request.method == 'POST' and organization:
        organization.name = request.POST.get('name')
        organization.city = request.POST.get('city')
        organization.district = request.POST.get('district')
        organization.street = request.POST.get('street')
        organization.building_number = request.POST.get('building_number')
        organization.contact_phone = request.POST.get('contact_phone')
        organization.contact_email = request.POST.get('contact_email')
        organization.save()

        departments_name = set(request.POST.getlist('departments_name'))
        positions_name = set(request.POST.getlist('positions_name'))

        positions_to_delete = [position for position in positions if position not in positions_name]
        departments_to_delete = [department for department in departments if department not in departments_name]
        Department.objects.filter(organization=organization, name__in=departments_to_delete).delete()
        Position.objects.filter(organization=organization, name__in=positions_to_delete).delete()

        positions_to_add = [position for position in positions_name if position not in positions]
        departments_to_add = [department for department in departments_name if department not in departments]
        for position in positions_to_add:
            position = Position(organization=organization, name=position)
            position.save()
        for department in departments_to_add:
            department = Department(organization=organization, name=department)
            department.save()

        return redirect('authorization:organizations')

    return render(request, 'authorization/edit-organization.html',
                  {
                      'organization': organization,
                      'departments': departments,
                      'positions': positions,
                  })


@login_required(login_url='authorization:login')
def organizations_view(request):
    organizations = Organization.objects.all()
    return render(request, 'authorization/organizations.html', {'organizations': organizations})
