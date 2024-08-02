import json

# Predefined dictionary of available products
AVAILABLE_PRODUCTS = {
    "widget": "Product is ready to manufacture",
    "gadget": "Product is ready to manufacture",
    "doodad": "Product is ready to manufacture"
}

def lambda_handler(event, context):
    body = json.loads(event['body'])
    product_name = body.get('productName', '').lower()
    
    if product_name in AVAILABLE_PRODUCTS:
        message = AVAILABLE_PRODUCTS[product_name]
    else:
        message = "Product is not available"
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': message}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }