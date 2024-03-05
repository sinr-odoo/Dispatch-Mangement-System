{
    'name': 'stock_transport',
    'depends': {
        'stock_picking_batch',
        'fleet'
    },
    'data':[
        "security/ir.model.access.csv",
        "views/fleet_vehicle_model_views.xml",
        "views/stock_picking_batch_views.xml",
        "views/stock_move_lines_views.xml"
    ],
    'application': True,
}