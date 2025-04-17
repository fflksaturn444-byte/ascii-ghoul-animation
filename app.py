import os
import time
from flask import Flask, Response, request

app = Flask(__name__)

input_folder = 'ascii' 
frame_count = 383 

def show_frame(frame_number):
    file_path = os.path.join(input_folder, f"{frame_number}.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            ascii_art = f.read()
            return ascii_art
    else:
        return f"clip {frame_number} not found"

def generate_animation():
    for frame in range(1, frame_count + 1):
        yield "data: \033c\n\n"
        
        ascii_art = show_frame(frame)
        yield f"data: {ascii_art}\n\n"
        time.sleep(0.1)
        
    ascii_art_saturn = """
 SSSSS  AAAAA  TTTTT  U   U  RRRR   N   N
S       A   A    T    U   U  R   R  NN  N
 SSS    AAAAA    T    U   U  RRRR   N N N
    S   A   A    T    U   U  R  R   N  NN
SSSS    A   A    T     UUU   R   R  N   N
            """
    yield f"{ascii_art_saturn}\n\n"

@app.route('/')
def index():
    return '''
    <html>
        <head><title>ASCII Animation</title></head>
        <body>
            <h1>Для просмотра используйте терминал с помощью curl</h1>
            <p>Для получения анимации, используйте команду:</p>
            <pre>curl link</pre>
        </body>
    </html>
    '''


@app.route('/anim')
def stream():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if 'curl' not in user_agent:
        return '''
        <html>
            <head><title>ASCII Animation</title></head>
            <body>
                <h1>Ошибка</h1>
                <p>Это работает только через терминал с помощью curl!</p>
            </body>
        </html>
        '''

    return Response(generate_animation(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)