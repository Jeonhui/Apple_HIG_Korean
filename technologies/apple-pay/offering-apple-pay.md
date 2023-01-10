# **[technologies-apple-pay] offering-apple-pay**

# **Offering Apple Pay as a payment option**
> Apple Pay를 결제 옵션으로 제공
>




**Offer Apple Pay on all devices that support it.** If the device doesn’t support Apple Pay, don’t present Apple Pay as a payment option.
> Apple Pay를 지원하는 모든 장치에서 Apple Pay를 제공합니다. 장치가 Apple Pay를 지원하지 않는 경우 Apple Pay를 결제 옵션으로 제공하지 마십시오.
>




**If you use Apple Pay APIs to find out whether the user has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs.** For example, you might pre-select Apple Pay as the payment option when you display it alongside other options. For developer guidance, see [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller) (iOS, watchOS) and [canMakePaymentsWithActiveCard](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778000-canmakepaymentswithactivecard?language=javascript) (web).
> Apple Pay API를 사용하여 사용자가 Wallet에 활성 카드를 가지고 있는지 여부를 확인하려면 API를 사용하는 모든 곳에서 Apple Pay를 기본 결제 옵션으로 설정해야 합니다. 예를 들어 다른 옵션과 함께 표시할 때 Apple Pay를 결제 옵션으로 미리 선택할 수 있습니다. 개발자 지침은 PK 지불을 참조하십시오인증 컨트롤러(iOS, watch)OS) 및 결제 가능ActiveCard(웹) 사용.
>




**If you also offer other payment methods, offer Apple Pay at the same time.** Feature Apple Pay at least as prominently as the other options on every page or screen that offers or accepts payment methods.
> 다른 결제 방법도 제공하는 경우 Apple Pay를 동시에 제공하십시오. Apple Pay는 결제 방법을 제공하거나 수락하는 모든 페이지 또는 화면의 다른 옵션과 마찬가지로 눈에 띄게 표시됩니다.
>




**If you use an Apple Pay button to trigger the Apple Pay payment process, you must use the Apple-provided API to display it.** Unlike a button graphic, the buttons produced by the API always have the correct appearance and are localized automatically. On devices running older systems that support Apple Pay on the web but don’t include the API, use the recommended CSS to display the buttons on your website, as described in [Displaying Apple Pay buttons](https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons).
> Apple Pay 버튼을 사용하여 Apple Pay 결제 프로세스를 트리거하는 경우 Apple에서 제공하는 API를 사용하여 표시해야 합니다. 버튼 그래픽과 달리 API에서 생성되는 버튼은 항상 올바른 모양을 가지며 자동으로 현지화됩니다. 웹에서 Apple Pay를 지원하지만 API를 포함하지 않는 이전 시스템을 실행하는 장치에서 Apple Pay 버튼 표시에 설명된 대로 권장 CSS를 사용하여 웹 사이트의 버튼을 표시합니다.
>




**If you use a custom button to trigger the Apple Pay payment process, make sure your custom button does not display “Apple Pay” or the Apple Pay logo.** In this scenario, you must let people know that you accept Apple Pay by displaying the Apple Pay mark or referencing Apple Pay in text on the same page that displays your payment button.
> 사용자 지정 버튼을 사용하여 Apple Pay 결제 프로세스를 트리거하는 경우 사용자 지정 버튼에 "Apple Pay" 또는 Apple Pay 로고가 표시되지 않도록 하십시오. 이 시나리오에서는 Apple Pay 마크를 표시하거나 Apple Pay를 텍스트로 참조하여 사용자가 Apple Pay를 수락한다는 사실을 사용자에게 알려야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Use Apple Pay buttons only to trigger the Apple Pay payment process and, when appropriate, the Apple Pay set up process.** When users choose an Apple Pay button to make a purchase, but their device doesn’t have Apple Pay set up, they’re given the opportunity to set up Apple Pay. Don’t use Apple Pay buttons in any other ways.
> Apple Pay 버튼은 Apple Pay 결제 프로세스와 적절한 경우 Apple Pay 설정 프로세스에만 사용하십시오. 사용자가 Apple Pay 버튼을 선택하여 구매를 수행하지만 장치에 Apple Pay가 설정되어 있지 않으면 Apple Pay를 설정할 수 있습니다. 다른 방법으로 Apple Pay 버튼을 사용하지 마십시오.
>




**Don’t disable or hide an Apple Pay button.** If an Apple Pay button can’t be used yet, such as when a product size or color hasn’t been selected, gracefully point out the problem after the user taps or clicks the button.
> Apple Pay 버튼을 비활성화하거나 숨기지 마십시오. 제품 크기나 색상을 선택하지 않은 경우와 같이 Apple Pay 버튼을 아직 사용할 수 없는 경우 사용자가 버튼을 누르거나 클릭한 후 문제를 올바르게 지적하십시오.
>




**Use the Apple Pay mark only to communicate that Apple Pay is accepted.** The [mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#apple-pay-mark) doesn’t facilitate payment. Never use it as a payment button or position it as a button. When using the Apple Pay mark to indicate Apple Pay as the selected payment method, you can create a separate custom button conforming to your app’s design to initiate the Apple Pay payment.
> Apple Pay 마크는 Apple Pay가 수락되었음을 알리기 위해서만 사용하십시오. 이 마크는 결제를 용이하게 하지 않습니다. 절대로 결제 버튼으로 사용하거나 버튼으로 위치하지 마십시오. Apple Pay 마크를 사용하여 Apple Pay를 선택한 결제 방법으로 표시할 때 Apple Pay 결제를 시작하기 위해 앱의 디자인에 맞는 별도의 사용자 지정 버튼을 만들 수 있습니다.
>




**Inform search engines that Apple Pay is accepted on your website.** If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.
> 검색 엔진에 Apple Pay가 사용자의 웹 사이트에서 승인되었음을 알립니다. 웹 사이트에서 의미 표시를 사용하여 검색 엔진에 제품 세부 정보를 제공하는 경우 Apple Pay를 결제 옵션으로 나열하십시오.
>




For app developer guidance, see [Apple Pay](https://developer.apple.com/documentation/passkit/apple_pay). For website developer guidance, including how to determine whether Apple Pay on the web is available, see [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web).
> 앱 개발자 지침은 Apple Pay를 참조하십시오. 웹에서 Apple Pay를 사용할 수 있는지 여부를 확인하는 방법을 포함한 웹 개발자 지침은 웹에서 Apple Pay를 참조하십시오.
>



