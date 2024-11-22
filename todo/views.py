from django.shortcuts import HttpResponse

def  task_create(request):
    html_response = """"
        <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Vazifa</title>
</head>
<body>
    <h1>Yangi vazifa yaratish</h1>
    <form action="#" method="post">
        <label for="vazifa-nomi">Vazifa nomi:</label>
        <br>
        <input type="text" id="vazifa-nomi" name="vazifa-nomi" required>
        <br><br>
        
        <label for="tavsif">Tavsif:</label>
        <br>
        <textarea id="tavsif" name="tavsif" rows="4" cols="50"></textarea>
        <br><br>
        
        <label for="muddat">Muddat:</label>
        <br>
        <input type="date" id="muddat" name="muddat">
        <br><br>
        
        <label for="muhimlik">Muhimlik darajasi:</label>
        <br>
        <select id="muhimlik" name="muhimlik">
            <option value="past">Past</option>
            <option value="o‘rta">O‘rta</option>
            <option value="yuqori">Yuqori</option>
        </select>
        <br><br>
        
        <button type="submit">Vazifani saqlash</button>
    </form>
</body>
</html>

    """

    return HttpResponse(html_response)
