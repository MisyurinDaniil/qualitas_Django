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

Fancybox.bind('[data-fancybox="tisnenie_page_1"]', {
    // Custom options for the first gallery
  });
Fancybox.bind('[data-fancybox="tisnenie_page_2"]', {
// Custom options for the first gallery
});

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

    mainButtonModal = document.querySelector('.main-button-modal');
    if (mainButtonModal) {
        mainButtonModal.addEventListener('click', () => {
            document.querySelector(".modal-window__content").classList.remove('display-none');
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

    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            let url = this.attributes.action.nodeValue;
            ajaxSend(formData, url)
                .then((response) => {
                    console.log(response);
                    // form.reset(); // очищаем поля формы
                    if (mainButtonModal) {
                        document.querySelector(".modal-window__content").classList.add('display-none')
                        document.querySelector(".modal-window__order-true").classList.remove('display-none')
                    }
                })
                .catch((err) => {
                    console.error(err)
                    if (mainButtonModal) {
                        document.querySelector(".modal-window__content").classList.add('display-none')
                        document.querySelector(".modal-window__order-false").classList.remove('display-none')
                    }
                });
        });
    });
}
