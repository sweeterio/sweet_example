from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.background import BackgroundTask
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
import uvicorn
from sweet import Sweet


app = Starlette()  #debug=True
app.mount('/report', StaticFiles(directory='report'))



async def suite(data):
    sweet = Sweet()
    sweet.run(data)
    del sweet


@app.route('/')
async def homepage(request):
    return FileResponse('index.html')

# @app.route('/')
# async def homepage(request):
#     return JSONResponse({'Sweet agent': '0.1'})


@app.route('/suite', methods=['POST'])
async def sweet(request):
    data = await request.json() 
    task = BackgroundTask(suite, data=data)    
    message = {'code': '0', 'message': 'Sweet is running'}
    return JSONResponse(message, background=task)

    
if __name__ == '__main__':
    print('start up')
    uvicorn.run(app, host='127.0.0.1', port=80)  # 如果要其他设备访问，请配置为： host='0.0.0.0'