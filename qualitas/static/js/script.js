const mainCarouselEl = document.querySelector('#mainCarousel');
const thumbCarouselEl = document.querySelector('#thumbCarousel');

if (mainCarouselEl && thumbCarouselEl) {
    const mainCarousel = new Carousel(mainCarouselEl, {
        Dots: false,
    });

    //Fancybox product slider
    // Thumbnails
    const thumbCarousel = new Carousel(thumbCarouselEl, {
        Sync: {
            target: mainCarousel,
            friction: 0,
        },
        Dots: false,
        Navigation: false,
        center: true,
        slidesPerPage: 1,
        infinite: false,
    });
    //
    //Fancybox product slider
    // Customize Fancybox
    Fancybox.bind('[data-fancybox="product_gallery"]', {
        Carousel: {
            on: {
                change: (that) => {
                    mainCarousel.slideTo(mainCarousel.findPageForSlide(that.page), {
                        friction: 0,
                    });
                },
            },
        },
    });
}


// isMobile. Проверяет зашел ли текущий пользователь с мобильного утсройства (планшет, телефон)
// Checks if the current user is logged in from a mobile device (tablet, phone)

let isMobile = {
    Android: function () {
        return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function () {
        return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function () {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function () {
        return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function () {
        return navigator.userAgent.match(/IEMobile/i);
    },
    any: function () {
        return (
            isMobile.Android() ||
            isMobile.BlackBerry() ||
            isMobile.iOS() ||
            isMobile.Opera() ||
            isMobile.Windows()
        );
    },
};

// Показывает или прячет выпладающее (sub-nav) меню (Каталог, Информация) для мобильных устройств
// Shows or hides the dropdown (sub-nav) menu (Catalog, Information) for mobile devices

let body = document.querySelector('body');
if (isMobile.any()) {
    body.classList.add('touch');

    subNavList = document.querySelectorAll('.sub-nav__list');
    for (let i = 0; i < subNavList.length; i++) {
        subNavList[i].parentNode.addEventListener('click', function (event) {
            event.stopImmediatePropagation();
            subNavList[i].classList.toggle('sub-nav__list-none');
            subNavList.forEach((element) => {
                if (subNavList[i] != element) {
                    element.classList.add('sub-nav__list-none');
                }
            });
        });
    }
} else {
    body.classList.add('mouse');
}

// Обработка события нажатия на кнопку бургреа.
// Показывает мобильную версию меню (nav)
let burger = document.querySelector('.burger');
burger.addEventListener('click', function () {
    if (isMobile.any()) {
        document.querySelector('.nav').classList.toggle('nav__display-none');
        document.querySelector('.nav').classList.toggle('overflow-auto');
        document.querySelector('body').classList.toggle('overflow-hidden');
    }
});

// Обработка события нажатия на кнопку закрытия мобильной версии меню.
// Прячет мобильную версию меню (nav)
closeButton = document.querySelector('.close-button');
closeButton.addEventListener('click', function () {
    if (isMobile.any()) {
        document.querySelector('.nav').classList.toggle('nav__display-none');
        document.querySelector('.nav').classList.toggle('overflow-auto');
        document.querySelector('body').classList.toggle('overflow-hidden');
    }
});

/********************************************/
/*************Отправка формы заказа *********/
/********************************************/

if (document.querySelector("form")) {
    
    let url = window.location.href;
    document.getElementById('id_order_product_url').value = url
    document.getElementById('review-form__product-url').value = url
    
    mainButtonModal = document.querySelector('.main-button-modal');

    if (mainButtonModal) {
        mainButtonModal.addEventListener('click', () => {
            document.querySelector(".modal-window__order").classList.remove('display-none');
            document.querySelector(".modal-window__order-true").classList.add('display-none');
            document.querySelector(".modal-window__order-false").classList.add('display-none');
        })
    }
    const ajaxSend = async (formData, url) => {
        const response = await fetch(url, {
            method: "POST",
            body: formData
        });
        if (!response.ok) {
            throw new Error(`Ошибка по адресу ${url}, статус ошибки ${response.status}`);
        }
        return await response.text();
    };

    const forms = document.querySelectorAll("form");

    // Добавляем отзыв без перезагрузки страницы
    function addReview(formData){
        let starsCounter = 0;
        let allStarsHTML = '';
        activateStarHTML = `
            <label class="stars__items--no-pointer">
                <div class="star-stroke star-stroke--background-col">
                    <div class="star-fill star-stroke--background-col"></div>
                </div>
            </label>
        `
        notActivateStarHTML = `
            <label class="stars__items--no-pointer">
                <div class="star-stroke">
                    <div class="star-fill"></div>
                </div>
            </label>
        `
        for (let i=0; i<5; i++) {
            if (starsCounter < formData.get('stars')) {
                starsCounter++;
                allStarsHTML = activateStarHTML + allStarsHTML;
                continue;
            }
            allStarsHTML = notActivateStarHTML + allStarsHTML;
        }

        var timeOptions = {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour:'numeric', 
            minute: 'numeric',
            timezone: 'UTC'
        };
        let subString  = ' в ';
        let dateStrForHTML = String(new Date().toLocaleString("ru", timeOptions)).replace(subString, ' ');

        var els = document.querySelectorAll('.old-review')
        var lastEl = els[els.length - 1];
        let newReview = `
            <div class="old-review">
            <div class="old-review__image-block">
                <img src="/static/img/user-icon-review.svg" alt="" class="old-review__img">
            </div>
            <div class="old-review__text">
                <div class="old-review__name-date-star__block">
                    <div class="old-review__name-date__block">
                        <p class="old-review__name">${formData.get('userName')}</p>
                        <p class="old-review__date">${dateStrForHTML}</p>
                    </div>
                    <div class="stars">
                        <div class="stars__items stars__items--align-item">
                            ${allStarsHTML}
                        </div>
                    </div>
                </div>
                <p class="old-review__message">
                    ${formData.get('text')}
                </p>
            </div>
            </div>
        `
        lastEl.insertAdjacentHTML('afterEnd', newReview);
    }

    function formsHandlers(form, response, formData) {
        // console.log(form);
        // console.log(form.id);
        console.log(response);
        if (form.id === "form-order") {
            if (response == "False") {
                document.querySelector(".modal-window__order").classList.add('display-none')
                document.querySelector(".modal-window__order-false").classList.remove('display-none')
            }
            if (response == "True") {
                form.reset()
                document.querySelector(".modal-window__order").classList.add('display-none')
                document.querySelector(".modal-window__order-true").classList.remove('display-none')
            }
        }
        if (form.id === "form-review") {
            if (response == "True") {
                form.reset()
                Fancybox.show([{ src: "#modal-window-review-true", type: "inline" }]);
                addReview(formData);
            }
            if (response == "False") {
                Fancybox.show([{ src: "#modal-window-review-false", type: "inline" }]);
            }
            if (response == "already_exists_client") {
                Fancybox.show([{ src: "#modal-window-review-al-ex-cl", type: "inline" }]);
            }
        }
    }

    forms.forEach((form) => {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            let url = this.attributes.action.nodeValue;
            ajaxSend(formData, url)
                .then((response) => {
                    formsHandlers(form, response, formData);
                })
                .catch((err) => {
                    console.error(err)
                    // !!!!!!!!!
                    // ДОбавлю функционал позже. Нужно закрыть все окна и открыть окно с ошибкой, сейчас не реализовано!!!!
                    // !!!!!!!!!
                    if (mainButtonModal) {
                        document.querySelector(".modal-window__order").classList.add('display-none')
                        document.querySelector(".modal-window__order-false").classList.remove('display-none')
                    }
                });
        });
    });

    // Валидация формы отрпавки отзыва (только количество звезд).
    // Проверяем на обязательность выбора количества звезд отзыва.
    // Показываем подсказку если количество звезд не указана пользователем.
    let submitReview = document.querySelector('.main-button__submit-review');
    if (submitReview) {
        submitReview.addEventListener('click', function(e){
            let formReview = document.getElementById('form-review');
            if(formReview.stars.value == '') {
                document.querySelector('.review-form__validation-prompt--stars').classList.remove('display-none');
            }
            if(formReview.stars.value != '') {
                document.querySelector('.review-form__validation-prompt--stars').classList.add('display-none');
            }
        })
    }

}
