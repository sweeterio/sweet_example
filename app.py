from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
import uvicorn


app = Starlette()  #debug=True
app.mount('/report', StaticFiles(directory='report'))


@app.route('/')
async def homepage(request):
    return FileResponse('index.html')

    
if __name__ == '__main__':
    print('start up')
    uvicorn.run(app, host='127.0.0.1', port=80)  # 如果要其他设备访问，请配置为： host='0.0.0.0'