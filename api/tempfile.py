import os

def handler(event, context):
    # Use /tmp directory for temporary storage
    temp_file_path = '/tmp/example.txt'

    # Write to the /tmp directory
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write('Hello, Vercel!')

    return {
        'statusCode': 200,
        'body': 'File written successfully to /tmp directory.'
    }
