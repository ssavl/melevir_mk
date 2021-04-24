



api_urls = [
    path('companies/', comp_view.CompanyViewSet.as_view({
        'get': 'list', 'post': 'create'
    }), name='companies-list'),
    path('companies/<int:company_id>/', comp_view.CompanyViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='companies-detail'),

    path('companies/<int:company_id>/ssds/', comp_view.SubdivisionViewSet.as_view({
        'get': 'list', 'post': 'create'
    }), name='subdivisions-list'),
    path('companies/<int:company_id>/ssds/<int:subdivision_id>/', comp_view.SubdivisionViewSet.as_view({
        'get': 'retrieve',  'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='subdivisions-detail'),
