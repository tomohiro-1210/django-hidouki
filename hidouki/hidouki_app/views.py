from django.shortcuts import render
import asyncio
from django.http import JsonResponse

# 非同期ビュー
async def async_view(request):
    mimic = "なんと宝箱はミミックだった！"
    today = "今日は寒かったけど、糀谷駅で京成3700形の後期車が見れたのはよかったな"
    context = {
        "mimic":mimic,
        "today":today,
               }
    await asyncio.sleep(2) # 非同期に２秒待機
    return JsonResponse({'message':'Hello, async Django!','context':context})

# テンプレート＋非同期ビュー
async def async_view2(request):
    template = 'index.html'
    async def async_task():
        
        # ２秒後にメッセージを返す非同期処理
        await asyncio.sleep(3)
        return "これは非同期処理の結果です"
    
    result = await async_task()
    context = {'message':result}
    
    return render(request, template, context)