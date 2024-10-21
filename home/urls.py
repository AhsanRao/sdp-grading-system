# from theme_soft_design import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index),
    path("about-us/", views.about_us, name="about-us"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("author/", views.author, name="author"),
    path("profile/", views.update_profile, name="update_profile"),
    # Authentication
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/student-register/", views.student_register, name="student_register"),
    path("accounts/faculty-register/", views.faculty_register, name="faculty_register"),
    path(
        "accounts/coordinator-register/",
        views.coordinator_register,
        name="coordinator_register",
    ),
    path("accounts/logout/", views.logout_view, name="logout"),
    path(
        "accounts/password-change/",
        views.UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "accounts/password-reset/",
        views.UserPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "accounts/password-reset-confirm/<uidb64>/<token>/",
        views.UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "coordinator/projects/",
        views.ProjectListView.as_view(),
        name="coordinator-project-list",
    ),
    path(
        "coordinator/projects/create/",
        views.ProjectCreateView.as_view(),
        name="coordinator-project-create",
    ),
    path(
        "coordinator/projects/<int:pk>/",
        views.ProjectDetailView.as_view(),
        name="coordinator-project-detail",
    ),
    path(
        "project/<int:pk>/delete/",
        views.ProjectDeleteView.as_view(),
        name="project-delete",
    ),
    path(
        "projects/<int:project_id>/groups/",
        views.GroupListView.as_view(),
        name="group-list",
    ),
    path(
        "coordinator/project/<int:pk>/group/create/",
        views.ProjectGroupCreateView.as_view(),
        name="project-group-create",
    ),
    path(
        "coordinator/project/group/<int:pk>/update/",
        views.ProjectGroupUpdateView.as_view(),
        name="project-group-update",
    ),
    path(
        "project/group/<int:pk>/delete/",
        views.ProjectGroupDeleteView.as_view(),
        name="project-group-delete",
    ),
    path(
        "project-group/<int:project_group_id>/assign-faculty/",
        views.AssignFacultyView.as_view(),
        name="assign-faculty",
    ),
    path(
        "faculty/projects/",
        views.FacultyProjectListView.as_view(),
        name="faculty-project-list",
    ),
    path(
        "faculty/projects/<int:project_id>/groups/",
        views.FacultyProjectGroupsView.as_view(),
        name="faculty-project-groups",
    ),
    path(
        "faculty/groups/<int:pk>/",
        views.FacultyGroupDetailView.as_view(),
        name="group-details",
    ),
    path(
        "logbook/<int:logbook_id>/entry/add/",
        views.LogbookEntryCreateView.as_view(),
        name="logbook-entry-add",
    ),
    path(
        "logbook/entry/<int:pk>/update/",
        views.LogbookEntryUpdateView.as_view(),
        name="logbook-entry-update",
    ),
    path(
        "project_group/<int:project_group_id>/proposal/add/",
        views.ProposalCreateView.as_view(),
        name="proposal-add",
    ),
    path(
        "proposal/<int:pk>/update/",
        views.ProposalUpdateView.as_view(),
        name="proposal-update",
    ),
    path(
        "project_group/<int:project_group_id>/add_progress_report/",
        views.ProgressReportCreateView.as_view(),
        name="add-progress-report",
    ),
    path(
        "project_group/<int:pk>/add_mid_project_report/",
        views.MidProjectReportCreateView.as_view(),
        name="add-mid-project-report",
    ),
    path(
        "project_group/<int:pk>/add_mid_project_presentation/",
        views.MidProjectPresentationCreateView.as_view(),
        name="add-mid-project-presentation",
    ),
    path(
        "project_group/<int:project_group_id>/reports/",
        views.ProjectReportsView.as_view(),
        name="project-reports",
    ),
    path(
        "faculty/projects/<int:project_group_id>/supervisor-reports/",
        views.ProjectReportsView.as_view(),
        name="supervisor-reports",
    ),
    path(
        "faculty/projects/<int:project_group_id>/examiner-reports/",
        views.ExaminarProjectReportsView.as_view(),
        name="examiner-reports",
    ),
    path(
        "student/projects/",
        views.StudentProjectListView.as_view(),
        name="student-project-list",
    ),
    path(
        "student/group/<int:group_id>/",
        views.StudentGroupDetailsView.as_view(),
        name="student-group-details",
    ),
    path(
        "student/project-reports/<int:project_group_id>/",
        views.StudentProjectReportsView.as_view(),
        name="student-project-reports",
    ),
    path(
        "projects/<int:project_group_id>/export/",
        views.export_supervisor_assessment,
        name="export-supervisor-assessment",
    ),
    path(
        "projects/<int:project_group_id>/export-examiner/",
        views.export_examiner_assesment,
        name="export-examiner-assessment",
    ),
]
