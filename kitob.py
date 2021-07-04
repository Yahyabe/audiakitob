import pyttsx3
import PyPDF2

with open ('qur.pdf', 'rb') as book:
    
    full_text = ""

    reader = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    voices = audio_reader.getProperty('voices')
    audio_reader.setProperty('voice', voices[0].id)


    audio_reader.setProperty("rate", 200)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content
    
    audio_reader.save_to_file(content, "mybook.mp3")
    audio_reader.runAndWait()
