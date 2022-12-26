# **[technologies-apple-pay] Buttons-and-marks**

The system provides several Apple Pay button types and styles you can use in your app or website. In contrast to the Apple Pay buttons, you use the [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks#apple-pay-mark) to communicate the availability of Apple Pay as a payment option.

Don’t create your own Apple Pay button design or attempt to mimic the system-provided button designs.

For related design guidance, see [Offering Apple Pay](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/offering-apple-pay/) and [Checkout and payment](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment/). For developer guidance, see [PKPaymentButtonType](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype) and [PKPaymentButtonStyle](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle) (iOS and macOS), [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) (watchOS), and [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web) (web).

# **Button types**

Apple provides several types of buttons so that you can choose the button type that fits best with the terminology and flow of your purchase or payment experience.

Use the Apple-provided APIs to create Apple Pay buttons. When you use the system-provided APIs, you get:

- A button that is guaranteed to use an Apple-approved caption, font, color, and style
- Assurance that the button’s contents maintain ideal proportions as you change its size
- Automatic translation of the button’s caption into the language that’s set for the device
- Support for configuring the button’s corner radius to match the style of your UI
- A system-provided alternative text label that lets VoiceOver describe the button

[제목 없음](https://www.notion.so/58811043153748f8a9a0b769c8d819ca)

When a device supports Apple Pay, but it hasn’t been set up yet, you can use the Set up Apple Pay button to show that Apple Pay is accepted and to give people an explicit opportunity to set it up.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/button-set-up_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/button-set-up_2x.png)

You can display the Set up Apple Pay button on pages such as a Settings page, a user profile screen, or an interstitial page. Tapping the button in any of these locations should initiate the process of adding a card.

# **Button styles**

Beginning in iOS 14 and macOS 11, you can use the  *automatic* style to let the current system appearance determine the appearance of the Apple Pay buttons in your app (for developer guidance, see [PKPaymentButtonStyle.automatic](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/automatic)). If you want to control the button appearance yourself, you can use one of the following options. For web developer guidance, see [ApplePayButtonStyle](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaybuttonstyle).

### **Black**

Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **White with outline**

Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t place on dark or saturated backgrounds.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **White**

Use on dark-color backgrounds that provide sufficient contrast.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

# **Button size and position**

**Prominently display the Apple Pay button.** Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-same-size-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-same-size-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-smaller-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-smaller-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Position the Apple Pay button correctly in relation to an Add to Cart button.** In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-right-side-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-right-side-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-left-side-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-left-side-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

In a stacked layout, place the Apple Pay button above an Add to Cart button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-top-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-top-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-below-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-below-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Adjust the corner radius to match the appearance of other buttons.** By default, an Apple Pay button has rounded corners. You can change the corner radius to produce a button with square corners or a pill-shaped button. For developer guidance, see [cornerRadius](https://developer.apple.com/documentation/passkit/pkpaymentbutton/2999416-cornerradius).

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-Corner-Radii_2x.png)

Minimum corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Default-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Default-Corner-Radii_2x.png)

Default corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Maximum-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Maximum-Corner-Radii_2x.png)

Maximum corner radius

**Maintain the minimum button size and margins around the button.** Be mindful that the button title may vary in length depending on the locale.

**NOTE**If the size you specify doesn’t accommodate the translated title for the type of payment button you’re using, the system automatically replaces it with the plain Apple Pay button shown below on the left. There is no automatic replacement for the Set up Apple Pay button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay-Donate_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay-Donate_2x.png)

Use the following values for guidance.

| Button | Minimum width | Minimum height | Minimum margins |
| --- | --- | --- | --- |
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Book with Apple PayBuy with Apple PayCheck out with Apple PayDonate with Apple PaySet up Apple PaySubscribe with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

# **Apple Pay mark**

Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other payment options in a similar manner. The Apple Pay mark is not a button; if you need an Apple Pay button, choose one of the buttons described in [Button types](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks#button-types). For design guidance related to showing Apple Pay as a payment option, see [Offering Apple Pay](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/offering-apple-pay/).

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayMarkWithPaymentOptions_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayMarkWithPaymentOptions_2x.png)

**Use only the artwork provided by Apple, with no alterations other than height.** You can specify a height for the Apple Pay mark, but make sure that the height you use is equal to or larger than other payment brand marks in your payment flow. Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t remove the border; don’t add visual effects to the mark, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the Apple Pay mark.

**Maintain a minimum clear space around the mark of 1/10 of its height.** Don’t let the Apple Pay mark share its surrounding border with another graphic or button.

Download the Apple Pay mark graphic and full usage guidelines [here](https://developer.apple.com/apple-pay/marketing/).