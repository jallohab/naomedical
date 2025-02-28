// Speech Recognition setup
const startBtn = document.getElementById("start-btn");
const originalText = document.getElementById("original-text");
const translatedText = document.getElementById("translated-text");
const speakTranslationBtn = document.getElementById("speak-translation");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';  // Set default language to English
recognition.continuous = true; // Keep listening until the user stops speaking
recognition.interimResults = true; // Show partial results

// Start recognition on button click
startBtn.addEventListener("click", () => {
    recognition.start();
});

// When speech is detected
recognition.onresult = async (event) => {
    let transcript = "";
    for (let i = event.resultIndex; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
    }
    originalText.textContent = transcript;

    // Translate the text after each speech result
    const translated = await translateText(transcript);
    translatedText.textContent = translated;
};

// Handle errors
recognition.onerror = (event) => {
    console.error("Error occurred in speech recognition: ", event.error);
};

// Function to call the translation API
async function translateText(text) {
    const targetLanguage = 'es'; // Example: translating to Spanish, you can make this dynamic
    const apiKey = 'YOUR_GOOGLE_TRANSLATE_API_KEY';
    const url = `https://translation.googleapis.com/language/translate/v2?key=${apiKey}`;

    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            q: text,
            target: targetLanguage,
        }),
        headers: {
            'Content-Type': 'application/json',
        },
    });

    const data = await response.json();
    return data.data.translations[0].translatedText;
}

// Function for audio playback of translated text
speakTranslationBtn.addEventListener("click", () => {
    const textToSpeak = translatedText.textContent;
    if (textToSpeak) {
        const utterance = new SpeechSynthesisUtterance(textToSpeak);
        utterance.lang = 'es-ES'; // Spanish, or set to the desired language
        window.speechSynthesis.speak(utterance);
    }
});