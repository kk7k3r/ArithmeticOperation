document.addEventListener("DOMContentLoaded", function () {
        const form = document.querySelector('.form'),
            form2 = document.querySelector('.form2'),
            form3 = document.querySelector('.form3'),
            page1 = document.querySelector('#page1'),
            page2 = document.querySelector('#page2'),
            page3 = document.querySelector('#page3'),
            inputName = document.querySelector('.inputName'),
            inputTries = document.querySelector('.inputTries'),
            inputAnswer = document.querySelector('.answer'),
            btnTry1More = document.querySelector('.btnTry1More'),
            btnNext = document.querySelector('.btnNext'),
            midResult = document.querySelector('.midResult'),
            equationText = document.querySelector('.equation'),
            subValue3 = document.querySelector('.subValue3'),
            mark = document.querySelector('.mark'),
            txtArea = document.querySelector('.txtArea'),
            successText = document.querySelector('.success-after-save-comment');

        let name = '', tries = 0, counter = 1, correctAnswer = '';
        let answers = ['', '', ''];
        let results = [0, 0, 0];

        btnNext.addEventListener('click', function () {
            page2.style.display = 'none';
            page3.style.display = 'block';

            // Заполнение таблицы результатов
            document.querySelector('.tdAnswer1').textContent = answers[0];
            document.querySelector('.corrAnswer1').textContent = correctAnswer;
            document.querySelector('.tdResult1').textContent = results[0];

            if (tries >= 2 && answers[1] !== '') {
                document.querySelector('.tr2').style.display = 'table-row';
                document.querySelector('.tdAnswer2').textContent = answers[1];
                document.querySelector('.corrAnswer2').textContent = correctAnswer;
                document.querySelector('.tdResult2').textContent = results[1];
            } else {
                document.querySelector('.tr2').style.display = 'none';
                document.querySelector('.tdAnswer2').textContent = '';
                document.querySelector('.corrAnswer2').textContent = '';
                document.querySelector('.tdResult2').textContent = '';
            }

            if (tries >= 3 && answers[2] !== '') {
                document.querySelector('.tr3').style.display = 'table-row';
                document.querySelector('.tdAnswer3').textContent = answers[2];
                document.querySelector('.corrAnswer3').textContent = correctAnswer;
                document.querySelector('.tdResult3').textContent = results[2];
            } else {
                document.querySelector('.tr3').style.display = 'none';
                document.querySelector('.tdAnswer3').textContent = '';
                document.querySelector('.corrAnswer3').textContent = '';
                document.querySelector('.tdResult3').textContent = '';
            }

            mark.textContent = (results[0] || results[1] || results[2]) ? 1 : 0;
        });

        form.addEventListener('submit', async function (e) {
            e.preventDefault();
            name = inputName.value;
            tries = parseInt(inputTries.value);
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name, tries})
            });
            const data = await response.json();
            equationText.innerHTML = data.equation;
            correctAnswer = data.correctAnswer;
            subValue3.textContent = data.base;
            page1.style.display = 'none';
            page2.style.display = 'block';
        });

        form2.addEventListener('submit', async function (e) {
            e.preventDefault();
            let userAnswer = inputAnswer.value;
            answers[counter - 1] = userAnswer;

            const response = await fetch('/check_answer', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({answer: userAnswer, correct_answer: correctAnswer})
            });
            const data = await response.json();

            results[counter - 1] = data.correct ? 1 : 0;
            midResult.textContent = data.correct ? 'Правильно' : 'Неправильно';

            if (data.correct) {
                page2.style.display = 'none';
                page3.style.display = 'block';

                document.querySelector('.tdAnswer1').textContent = answers[0];
                document.querySelector('.corrAnswer1').textContent = correctAnswer;
                document.querySelector('.tdResult1').textContent = results[0];

                if (tries >= 2 && answers[1] !== '') {
                    document.querySelector('.tr2').style.display = 'table-row';
                    document.querySelector('.tdAnswer2').textContent = answers[1];
                    document.querySelector('.corrAnswer2').textContent = correctAnswer;
                    document.querySelector('.tdResult2').textContent = results[1];
                } else {
                    document.querySelector('.tr2').style.display = 'none';
                    document.querySelector('.tdAnswer2').textContent = '';
                    document.querySelector('.corrAnswer2').textContent = '';
                    document.querySelector('.tdResult2').textContent = '';
                }

                if (tries >= 3 && answers[2] !== '') {
                    document.querySelector('.tr3').style.display = 'table-row';
                    document.querySelector('.tdAnswer3').textContent = answers[2];
                    document.querySelector('.corrAnswer3').textContent = correctAnswer;
                    document.querySelector('.tdResult3').textContent = results[2];
                } else {
                    document.querySelector('.tr3').style.display = 'none';
                    document.querySelector('.tdAnswer3').textContent = '';
                    document.querySelector('.corrAnswer3').textContent = '';
                    document.querySelector('.tdResult3').textContent = '';
                }

                mark.textContent = (results[0] || results[1] || results[2]) ? 1 : 0;
                return;
            }

            if (counter >= tries) {
                btnTry1More.disabled = true;
                btnTry1More.style.background = '#646262';
                btnNext.style.display = 'block';
            }
            counter++;
        });

        form3.addEventListener('submit', async function (e) {
            e.preventDefault();
            const now = new Date();
            const timeString = now.toLocaleString();
            const surname = name.split(' ')[0] || name;
            const commentValue = txtArea.value;
            let tableText = 'Попытка №\tВаш ответ\tПравильный ответ\tРезультат\n';
            if (answers[0] !== '') tableText += `1\t\t${answers[0]}\t\t${correctAnswer}\t\t\t${results[0]}\n`;
            if (tries >= 2 && answers[1] !== '') tableText += `2\t\t${answers[1]}\t\t${correctAnswer}\t\t\t${results[1]}\n`;
            if (tries >= 3 && answers[2] !== '') tableText += `3\t\t${answers[2]}\t\t${correctAnswer}\t\t\t${results[2]}\n`;

            const response = await fetch('/save_result', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    table: tableText,
                    surname: surname,
                    comment: commentValue,
                    time: timeString
                })
            });
            const data = await response.json();
            if (data.status === "ok") {
                const a = document.createElement('a');
                a.href = `/download_result/${data.filename}`;
                a.download = data.filename;
                document.body.appendChild(a);
                a.click();
                setTimeout(function () {
                    document.body.removeChild(a);
                }, 0);
                successText.style.display = 'block';
            }
        });
    });