from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections # type: ignore
import nltk # type: ignore
import random

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')

app = Flask(__name__)

# Define pairs of patterns and responses
pairs = [
    # General greetings and introductions
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!"]],
    [r"what is your name?", ["I am InfiPsy, your virtual assistant created by BMS."]],
    [r"how are you?", ["I'm here to assist you. How can I help you today?"]],
    [r"sorry (.*)", ["It's okay, no worries!"]],
    [r"I am (.*) (good|well|okay|ok)", ["Good to hear that!"]],
    [r"how (.*) work?", ["I process your inputs and respond accordingly."]],
    [r"(.*) created you?", ["I was created by the BMS team."]],
    [r"quit", ["Goodbye! It was nice talking to you."]],

    # Anxiety-related responses
    [r"what should I do if I feel anxious?", ["There are many ways to cope with anxiety, including deep breathing exercises, talking to someone you trust, and practicing mindfulness."]],
    [r"how can I manage anxiety?", ["Managing anxiety can include regular exercise, maintaining a healthy diet, practicing relaxation techniques, and seeking professional help if needed."]],
    [r"why do I feel anxious all the time?", ["Persistent anxiety can have various causes, including stress, past trauma, or underlying health issues. It's important to talk to a mental health professional for personalized advice."]],
    [r"how to stop feeling anxious?", ["To reduce anxiety, you can try relaxation techniques, such as deep breathing and mindfulness exercises. It's also helpful to identify triggers and practice self-care."]],

    # Depression-related responses
    [r"(.*) depression?", ["Depression is a common mental health issue. It's important to seek professional help if you're experiencing symptoms of depression."]],
    [r"how can I deal with depression?", ["Dealing with depression often requires a combination of therapy, medication, and lifestyle changes. Regular exercise, a balanced diet, and staying connected with loved ones can also help."]],
    [r"what are the symptoms of depression?", ["Symptoms of depression can include persistent sadness, loss of interest in activities, changes in appetite or sleep patterns, and feelings of hopelessness or worthlessness."]],
    [r"how to overcome depression?", ["Overcoming depression involves seeking support from professionals, engaging in activities you enjoy, setting realistic goals, and taking care of your physical and emotional well-being."]],

    # Stress-related responses
    [r"how can I reduce stress?", ["Reducing stress can involve practicing relaxation techniques like deep breathing, meditation, or yoga. Regular physical activity, maintaining a healthy diet, and ensuring adequate sleep are also important."]],
    [r"why am I so stressed?", ["Stress can be caused by various factors, such as work pressure, personal relationships, or health concerns. Identifying stressors and finding effective coping strategies is essential for managing stress."]],
    [r"what are some stress management techniques?", ["Effective stress management techniques include time management, setting boundaries, prioritizing tasks, and seeking social support."]],
    [r"how to relax when stressed?", ["To relax when stressed, try activities like listening to music, taking a walk, practicing deep breathing exercises, or engaging in hobbies that you enjoy."]],

    # Relationship-related responses
    [r"how can I improve my relationship with my partner?", ["Improving relationships involves effective communication, mutual respect, spending quality time together, and resolving conflicts constructively."]],
    [r"why do I have relationship problems?", ["Relationship problems can arise from issues like poor communication, trust issues, conflicting values, or lack of emotional intimacy. Seeking counseling can help address these issues."]],
    [r"how to cope with a breakup?", ["Coping with a breakup can be challenging. It's important to give yourself time to heal, seek support from friends and family, and engage in self-care activities to promote emotional recovery."]],

    # Self-care and well-being responses
    [r"what are good self-care practices?", ["Self-care practices include prioritizing sleep, eating nutritious meals, exercising regularly, setting boundaries, and engaging in activities that promote relaxation and well-being."]],
    [r"how to practice self-care?", ["Self-care involves making time for activities that nurture your physical, emotional, and mental health. This includes setting aside time for relaxation, hobbies, and seeking support when needed."]],
    [r"why is self-care important?", ["Self-care is essential for maintaining overall well-being and resilience. It helps reduce stress, prevent burnout, and enhance your ability to cope with challenges effectively."]],
    [r"how to improve mental health?", ["Improving mental health involves adopting healthy lifestyle habits, seeking support from loved ones or professionals, setting realistic goals, and practicing self-compassion."]],

    # Aging-related responses
    [r"how can older adults maintain mental health?", ["Older adults can maintain mental health by staying physically active, engaging in social activities, pursuing hobbies, and seeking support from peers or professionals."]],
    [r"how to cope with loneliness in old age?", ["Coping with loneliness in old age involves staying connected with friends and family, joining community groups, volunteering, and exploring new interests or hobbies."]],
    [r"what are common mental health concerns for seniors?", ["Common mental health concerns for seniors include depression, anxiety, cognitive decline, and adjustment to life changes. Regular medical check-ups and social engagement are important for early detection and support."]],

    # Teenager-related responses
    [r"how can teenagers manage stress?", ["Teenagers can manage stress by practicing relaxation techniques, maintaining a balanced schedule, seeking support from friends or adults, and engaging in activities they enjoy."]],
    [r"what are signs of anxiety in teenagers?", ["Signs of anxiety in teenagers include excessive worry, irritability, difficulty concentrating, physical symptoms like headaches or stomachaches, and avoidance of certain situations."]],
    [r"how to support a teenager with mental health issues?", ["Supporting a teenager with mental health issues involves listening without judgment, encouraging open communication, seeking professional help if needed, and promoting a healthy lifestyle."]],

    # Additional general insights
    [r"what is mindfulness?", ["Mindfulness is the practice of being present in the moment without judgment. It involves paying attention to thoughts, feelings, and sensations with acceptance and curiosity."]],
    [r"how to practice mindfulness?", ["You can practice mindfulness through meditation, deep breathing exercises, or simply by focusing on your senses and being aware of your surroundings."]],
    [r"why is therapy important?", ["Therapy provides a safe space to explore thoughts and emotions, learn coping strategies, gain insights into behavior patterns, and work towards personal growth and healing."]],
    [r"how does therapy help?", ["Therapy helps by providing support, guidance, and tools to manage stress, improve relationships, cope with challenges, and enhance overall well-being."]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)