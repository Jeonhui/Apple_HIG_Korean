# **[technologies-apple-pay] introduction**

# Apple Pay is a secure, easy way to make payments for physical goods and services — as well as donations and subscriptions — in apps running on iPhone, iPad, Mac, and Apple Watch, and on websites.
> 애플 페이(Apple Pay)는 아이폰, 아이패드, 맥, 애플 워치, 웹사이트에서 실행되는 앱에서 기부와 구독뿐만 아니라 물리적인 상품과 서비스에 대한 지불을 안전하고 쉬운 방법이다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Apple-Pay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Apple-Pay-intro_2x.png)

People authorize payments and provide shipping and contact information, using credentials that are securely stored on the device.
> 사람들은 기기에 안전하게 저장된 자격 증명을 사용하여 결제를 승인하고 배송 및 연락처 정보를 제공합니다.
>




**TIP**It’s important to understand the difference between Apple Pay and [In-App Purchase](../technologies/in-app-purchase/introduction). Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and tickets for events; and for donations. Use In-App Purchase in your app to sell virtual goods, such as premium content for your app, and subscriptions for digital content.
> TIP Apple Pay와 In-App Purchase의 차이점을 이해하는 것이 중요합니다. Apple Pay를 사용하여 식료품, 의류 및 가전제품과 같은 실물 상품을 판매하고, 클럽 회원권, 호텔 예약, 이벤트 티켓과 같은 서비스를 제공하며, 기부를 할 수 있습니다. 앱에서 앱 내 구매를 사용하여 앱의 프리미엄 콘텐츠 및 디지털 콘텐츠 구독과 같은 가상 상품을 판매하십시오.
>




# **Apple Pay in apps**

Apps that accept Apple Pay display an [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#apple-pay-mark) wherever available payment options are shown and an [Apple Pay button](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#button-types) that people tap to bring up a [payment sheet](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment/#customize-the-payment-sheet). During [checkout](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment/#streamline-the-checkout-process), the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments and then authorize payment and complete the purchase.
> Apple Pay를 사용할 수 있는 앱은 사용 가능한 결제 옵션이 표시되는 곳마다 Apple Pay 마크와 사람들이 결제 시트를 불러오기 위해 누르는 Apple Pay 버튼을 표시합니다. 결제 시트는 체크아웃 시 Apple Pay에 연결된 신용 카드 또는 직불 카드, 구매 금액(세금 및 수수료 포함), 배송 옵션 및 연락처 정보를 표시할 수 있습니다. 사람들은 필요한 조정을 한 다음 지불을 승인하고 구매를 완료합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet_2x.png)

For developer guidance, see [PassKit > Apple Pay](https://developer.apple.com/documentation/passkit/apple_pay).
> 개발자 지침은 PassKit > Apple Pay를 참조하십시오.
>




# **Apple Pay on the web**
> 웹상의 애플 페이
>




Websites that accept Apple Pay incorporate it into the purchasing flow. An [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#apple-pay-mark) should be shown wherever available payment options are shown and an [Apple Pay button](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#button-types) can be clicked to bring up a [payment sheet](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment/#customize-the-payment-sheet). During [checkout](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment/#streamline-the-checkout-process), the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments, authorize payment, and complete the purchase using securely stored credentials on iPhone, iPad, and Macs that include Touch ID or a Magic Keyboard with Touch ID (for a complete list of supported Macs, see [Apple Pay is compatible with these devices](https://support.apple.com/en-us/HT208531)). On other Macs, people confirm the purchase with their nearby iPhone or Apple Watch that has Apple Pay enabled.
> 애플 페이를 받아들이는 웹사이트들은 애플 페이를 구매 흐름에 포함시킨다. 사용 가능한 결제 옵션이 표시되는 곳마다 Apple Pay 마크가 표시되어야 하며 Apple Pay 버튼을 클릭하여 결제 시트를 불러올 수 있습니다. 결제 시트는 체크아웃 시 Apple Pay에 연결된 신용 카드 또는 직불 카드, 구매 금액(세금 및 수수료 포함), 배송 옵션 및 연락처 정보를 표시할 수 있습니다. 사람들은 터치 ID 또는 터치 ID가 포함된 Magic Keyboard를 포함한 iPhone, iPad 및 Mac에 안전하게 저장된 자격 증명을 사용하여 필요한 모든 조정을 수행하고 결제를 승인하며 구매를 완료합니다(지원되는 Mac의 전체 목록은 Apple Pay가 이러한 장치와 호환됨을 참조하십시오). 다른 맥에서는 애플 페이가 활성화된 근처의 아이폰이나 애플 워치로 구매를 확인한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/applePayHero_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/applePayHero_2x.png)

All websites that offer Apple Pay must include a privacy statement and adhere to the [Apple Pay on the web acceptable use guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/). For developer guidance, see [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web). For a hands-on demo of Apple Pay on the web, see [Apple Pay on the web demo](https://applepaydemo.apple.com/).
> Apple Pay를 제공하는 모든 웹 사이트는 개인 정보 보호 정책을 포함해야 하며 웹에서 허용되는 사용 지침에 Apple Pay를 준수해야 합니다. 개발자 지침은 웹에서 Apple Pay를 참조하십시오. 웹에서 Apple Pay의 실습 데모를 보려면 웹 데모에서 Apple Pay를 참조하십시오.
>



