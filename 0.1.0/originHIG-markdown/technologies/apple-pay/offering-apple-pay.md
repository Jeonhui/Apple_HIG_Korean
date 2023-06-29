# **[technologies-apple-pay] offering-apple-pay**

# **Offering Apple Pay as a payment option**

**Offer Apple Pay on all devices that support it.** If the device doesn’t support Apple Pay, don’t present Apple Pay as a payment option.

**If you use Apple Pay APIs to find out whether the user has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs.** For example, you might pre-select Apple Pay as the payment option when you display it alongside other options. For developer guidance, see [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller) (iOS, watchOS) and [canMakePaymentsWithActiveCard](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778000-canmakepaymentswithactivecard?language=javascript) (web).

**If you also offer other payment methods, offer Apple Pay at the same time.** Feature Apple Pay at least as prominently as the other options on every page or screen that offers or accepts payment methods.

**If you use an Apple Pay button to trigger the Apple Pay payment process, you must use the Apple-provided API to display it.** Unlike a button graphic, the buttons produced by the API always have the correct appearance and are localized automatically. On devices running older systems that support Apple Pay on the web but don’t include the API, use the recommended CSS to display the buttons on your website, as described in [Displaying Apple Pay buttons](https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons).

**If you use a custom button to trigger the Apple Pay payment process, make sure your custom button does not display “Apple Pay” or the Apple Pay logo.** In this scenario, you must let people know that you accept Apple Pay by displaying the Apple Pay mark or referencing Apple Pay in text on the same page that displays your payment button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/custom-button-no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Use Apple Pay buttons only to trigger the Apple Pay payment process and, when appropriate, the Apple Pay set up process.** When users choose an Apple Pay button to make a purchase, but their device doesn’t have Apple Pay set up, they’re given the opportunity to set up Apple Pay. Don’t use Apple Pay buttons in any other ways.

**Don’t disable or hide an Apple Pay button.** If an Apple Pay button can’t be used yet, such as when a product size or color hasn’t been selected, gracefully point out the problem after the user taps or clicks the button.

**Use the Apple Pay mark only to communicate that Apple Pay is accepted.** The [mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/#apple-pay-mark) doesn’t facilitate payment. Never use it as a payment button or position it as a button. When using the Apple Pay mark to indicate Apple Pay as the selected payment method, you can create a separate custom button conforming to your app’s design to initiate the Apple Pay payment.

**Inform search engines that Apple Pay is accepted on your website.** If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.

For app developer guidance, see [Apple Pay](https://developer.apple.com/documentation/passkit/apple_pay). For website developer guidance, including how to determine whether Apple Pay on the web is available, see [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web).