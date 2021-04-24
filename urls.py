



api_urls = [
    path('users/', UsersViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='users-list'),
    
    path('companies/<int:company_id>/', comp_view.UsersViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='user-detail'),

    path('add/', AddViewSet.as_view({
       'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='ad-list'),
    
    path('add/<int:company_id>/', AdViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='ad-detail'),
    
    path('add/<int:company_id>/', AdViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='ad-detail'),
    
    path('add/<int:company_id>/', AdViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='ad-detail'),
    
