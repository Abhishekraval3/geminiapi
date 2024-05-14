from django.shortcuts import render
import google.generativeai as genai
import markdown
from PIL import Image

gemini_api_key = 'AIzaSyAff7meN7yovdnPVpQOGxvja4XDT7tNW6A'
genai.configure(api_key = gemini_api_key)
model = genai.GenerativeModel('gemini-pro-vision')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def prediction(request):
    if request.method == 'POST':
        img = request.FILES['image']
        img_obj = Image.open(img)
        response = model.generate_content(["Solve the Multiple choice Questions and display only the answers With there option", img_obj], stream=True)
        response.resolve()
        markdown_text = markdown.markdown(response.text)
        print(markdown_text)
        return render(request, 'index.html',{'ans' : markdown_text})
    else:
        return render(request, 'index.html' )