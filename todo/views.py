from django.shortcuts import HttpResponse

def  task_create(request):
    html_response = """
    <title>Add Vazifa</title>
    <h1>Yangi vazifa yaratish</h1>
        <label>Vazifa nomi:</label>
        <input type="text" required>
        <br><br>
        
        <label>Tavsif:</label>
        <textarea rows="4" cols="50"></textarea>
        <br><br>
        
        <label>Muddat:</label>
        <input type="date">
        <br><br>
        
        <label>Muhimlik darajasi:</label>
        <select>
            <option>Past</option>
            <option>O‘rta</option>
            <option>Yuqori</option>
        </select>
        <br><br>
        
        <button>Saqlash</button>
    """

    return HttpResponse(html_response)
