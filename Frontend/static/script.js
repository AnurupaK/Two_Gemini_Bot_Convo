document.addEventListener('DOMContentLoaded', function () {
    const gemiDropdown = document.getElementById('gemi_drop');
    const gemoDropdown = document.getElementById('gemo_drop');
    const promptLinks = document.querySelectorAll('.drop a');

    let gemiSelectedPrompt = null;
    let gemoSelectedPrompt = null;

    console.log(gemiDropdown, gemoDropdown);
    console.log(promptLinks);

    promptLinks.forEach((link) => {
        console.log(link);
        link.addEventListener('click', async function (event) {
            event.preventDefault();  // To stop the clicking event on the link

            const selectedPrompt = this.getAttribute('data-prompt');
            console.log(`I am selected ${selectedPrompt}`);

            // Check which dropdown the clicked link belongs to
            if (this.parentElement.id === 'gemi_drop') {
                gemiSelectedPrompt = selectedPrompt;
                gemiDropdown.style.display = 'none';
            } else if (this.parentElement.id === 'gemo_drop') {
                gemoSelectedPrompt = selectedPrompt;
                gemoDropdown.style.display = 'none';
            }

            console.log(`From gemi: ${gemiSelectedPrompt}`);
            console.log(`From gemo: ${gemoSelectedPrompt}`);

            if (gemiSelectedPrompt && gemoSelectedPrompt) {
                const message = "Not sent";
                const isSent = await sendPrompts(gemiSelectedPrompt, gemoSelectedPrompt, message);
                console.log(isSent);

                if (isSent === 'Sent successfully') {
                    let round = 7;
                    for (let i = 0; i < round; i++) {
                        const responses = await getBotresponses();
                        console.log(responses);

                        const screen = document.querySelector('.screen');

                        // Gemi Bot response
                        await showBotResponse('gemi', responses.gemiResponse, screen);

                        // Gemo Bot response
                        await showBotResponse('gemo', responses.gemoResponse, screen);
                    }
                } else {
                    console.error("Prompts are not yet sent to backend");
                    const screen2 = document.querySelector('.screen');
                    let gemoBot = document.createElement('div');
                    gemoBot.className = 'chat-message gemoTxt';
                    gemoBot.innerHTML = `<span class='emoji' style='font-size: 30px;'>😔</span><p>Prompts are not yet sent to backend</p>`;
                    screen2.appendChild(gemoBot);
                }
            } else {
                console.log('Waiting for both prompts to be selected');
            }
        });
    });
});

async function sendPrompts(gemiSelectedPrompt, gemoSelectedPrompt, message) {
    try {
        let response_if_send = await fetch('/api/sendPrompt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ gemiSelectedPrompt, gemoSelectedPrompt, message })
        });

        let data = await response_if_send.json();
        console.log(data);
        return data.message;  
    } catch (error) {
        console.error('Error:', error);
    }
}

async function getBotresponses() {
    try {
        let responses = await fetch('/api/get_response_fromBots', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        let data = await responses.json();
        return {
            gemiResponse: data.gemi,
            gemoResponse: data.gemo
        };
    } catch (error) {
        console.log('Error in response:', error);
        return {
            gemiResponse: 'Oops! I can\'t say Gemo',
            gemoResponse: 'Oops! I can\'t say Gemi'
        };
    }
}

async function showBotResponse(botType, responseText, screen) {
    let botEmoji = botType === 'gemi' ? '🐥' : '🐧';
    let botClass = botType === 'gemi' ? 'gemiTxt' : 'gemoTxt';

    let bot = document.createElement('div');
    bot.className = `chat-message ${botClass}`;
    bot.innerHTML = `<span class='emoji' style='font-size: 30px;'>${botEmoji}</span>`;
    screen.appendChild(bot);

    let interval = addDotsEffect(bot);

    await new Promise((resolve) => setTimeout(resolve, 3000));  
    clearInterval(interval);  

    bot.innerHTML = `<span class='emoji' style='font-size: 30px;'>${botEmoji}</span>`;
    await typeEffect(bot, responseText);  
    console.log(`${botType.charAt(0).toUpperCase() + botType.slice(1)} message appended`);
}

function addDotsEffect(element) {
    let dotCount = 0;
    let originalText = element.innerHTML;

    let intervalId = setInterval(() => {
        element.innerHTML = originalText + `<span style='font-size: 50px;'>${'.'.repeat(dotCount)}</span>`;
        dotCount = (dotCount + 1) % 5;  
    }, 300);

    return intervalId;
}

async function typeEffect(element, text) {
    const typingSpeed = 50;  
    let i = 0;

    while (i < text.length) {
        element.innerHTML += text.charAt(i);
        i++;
        await new Promise((resolve) => setTimeout(resolve, typingSpeed));
    }
}
