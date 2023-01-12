# **[technologies-apple-pay] Buttons-and-marks**

The system provides several Apple Pay button types and styles you can use in your app or website. In contrast to the Apple Pay buttons, you use the [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks#apple-pay-mark) to communicate the availability of Apple Pay as a payment option.
> 이 시스템은 앱이나 웹 사이트에서 사용할 수 있는 몇 가지 Apple Pay 버튼 유형과 스타일을 제공합니다. Apple Pay 버튼과 달리 Apple Pay 마크를 사용하여 Apple Pay를 결제 옵션으로 사용할 수 있음을 알 수 있습니다.
>




Don’t create your own Apple Pay button design or attempt to mimic the system-provided button designs.
> Apple Pay 버튼 디자인을 직접 만들거나 시스템에서 제공하는 버튼 디자인을 모방하지 마십시오.
>




For related design guidance, see [Offering Apple Pay](../technologies/apple-pay/offering-apple-pay/) and [Checkout and payment](../technologies/apple-pay/checkout-and-payment/). For developer guidance, see [PKPaymentButtonType](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype) and [PKPaymentButtonStyle](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle) (iOS and macOS), [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) (watchOS), and [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web) (web).
> 관련 설계 지침은 Apple Pay 및 체크아웃 및 결제 제공을 참조하십시오. 개발자 지침은 웹(웹)에서 PKPaymentButtonType 및 PKPaymentButtonStyle(iOS 및 macOS), WKInterfacePayButton(watchOS) 및 ApplePay를 참조하십시오.
>




# **Button types**

Apple provides several types of buttons so that you can choose the button type that fits best with the terminology and flow of your purchase or payment experience.
> Apple은 여러 유형의 버튼을 제공하므로 구입 또는 결제 경험의 용어와 흐름에 가장 적합한 버튼 유형을 선택할 수 있습니다.
>




Use the Apple-provided APIs to create Apple Pay buttons. When you use the system-provided APIs, you get:
> Apple에서 제공하는 API를 사용하여 Apple Pay 버튼을 만듭니다. 시스템에서 제공하는 API를 사용하면 다음과 같은 이점을 얻을 수 있습니다:
>




- A button that is guaranteed to use an Apple-approved caption, font, color, and style
- >  Apple에서 승인한 캡션, 글꼴, 색상 및 스타일을 사용할 수 있는 단추

- Assurance that the button’s contents maintain ideal proportions as you change its size
- >  버튼 크기를 변경해도 버튼 내용이 이상적인 비율을 유지하도록 보장

- Automatic translation of the button’s caption into the language that’s set for the device
- >  단추의 캡션을 장치에 설정된 언어로 자동 변환

- Support for configuring the button’s corner radius to match the style of your UI
- >  UI 스타일에 맞게 버튼 모서리 반지름 구성 지원

- A system-provided alternative text label that lets VoiceOver describe the button
- >  VoiceOver가 버튼을 설명할 수 있도록 시스템에서 제공하는 대체 텍스트 레이블


[제목 없음](https://www.notion.so/58811043153748f8a9a0b769c8d819ca)

When a device supports Apple Pay, but it hasn’t been set up yet, you can use the Set up Apple Pay button to show that Apple Pay is accepted and to give people an explicit opportunity to set it up.
> 장치가 Apple Pay를 지원하지만 아직 설정되지 않은 경우 Apple Pay 설정 단추를 사용하여 Apple Pay가 승인되었음을 표시하고 사용자에게 Apple Pay를 설정할 수 있는 명시적인 기회를 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/button-set-up_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/button-set-up_2x.png)

You can display the Set up Apple Pay button on pages such as a Settings page, a user profile screen, or an interstitial page. Tapping the button in any of these locations should initiate the process of adding a card.
> 설정 페이지, 사용자 프로필 화면 또는 중간 페이지와 같은 페이지에 Apple Pay 설정 버튼을 표시할 수 있습니다. 이러한 위치에서 버튼을 누르면 카드 추가 프로세스가 시작됩니다.
>




# **Button styles**

Beginning in iOS 14 and macOS 11, you can use the  *automatic* style to let the current system appearance determine the appearance of the Apple Pay buttons in your app (for developer guidance, see [PKPaymentButtonStyle.automatic](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/automatic)). If you want to control the button appearance yourself, you can use one of the following options. For web developer guidance, see [ApplePayButtonStyle](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaybuttonstyle).
> iOS 14 및 macOS 11부터는 자동 스타일을 사용하여 현재 시스템 모양이 앱에서 Apple Pay 버튼의 모양을 결정하도록 할 수 있습니다(개발자 지침은 PKPaymentButtonStyle.automatic 참조). 단추 모양을 직접 제어하려면 다음 옵션 중 하나를 사용할 수 있습니다. 웹 개발자 지침은 ApplePayButtonStyle을 참조하십시오.
>




### **Black**

Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.
> 흰색 또는 밝은 색상 배경에 사용하여 충분한 대비를 제공합니다. 검은색이나 어두운 배경에는 사용하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_black_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **White with outline**

Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t place on dark or saturated backgrounds.
> 대비가 충분하지 않은 흰색 또는 밝은 색상 배경에 사용합니다. 어둡거나 포화된 배경에 두지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_outline_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **White**

Use on dark-color backgrounds that provide sufficient contrast.
> 충분한 대비를 제공하는 어두운 색상의 배경에 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay_white_no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

# **Button size and position**

**Prominently display the Apple Pay button.** Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.
> Apple Pay 버튼을 눈에 띄게 표시합니다. Apple Pay 버튼을 다른 결제 버튼보다 작지 않게 설정하고, 사람들이 스크롤하여 볼 수 없도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-same-size-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-same-size-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-smaller-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-smaller-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Position the Apple Pay button correctly in relation to an Add to Cart button.** In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button.
> 카트에 추가 버튼을 기준으로 Apple Pay 버튼을 올바르게 배치합니다. 나란히 배치할 경우 카트에 추가 버튼의 오른쪽에 Apple Pay 버튼을 배치합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-right-side-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-right-side-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-left-side-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-left-side-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

In a stacked layout, place the Apple Pay button above an Add to Cart button.
> 쌓인 레이아웃에서 애플 페이 버튼을 카트에 추가 버튼 위에 놓습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-top-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-top-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-below-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ap-below-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

**Adjust the corner radius to match the appearance of other buttons.** By default, an Apple Pay button has rounded corners. You can change the corner radius to produce a button with square corners or a pill-shaped button. For developer guidance, see [cornerRadius](https://developer.apple.com/documentation/passkit/pkpaymentbutton/2999416-cornerradius).
> 다른 단추의 모양에 맞게 모서리 반지름을 조정합니다. 기본적으로 Apple Pay 단추에는 둥근 모서리가 있습니다. 모서리 반지름을 변경하여 모서리가 사각형인 단추나 알약 모양의 단추를 만들 수 있습니다. 개발자 지침은 코너 Radius를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-Corner-Radii_2x.png)

Minimum corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Default-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Default-Corner-Radii_2x.png)

Default corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Maximum-Corner-Radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Maximum-Corner-Radii_2x.png)

Maximum corner radius

**Maintain the minimum button size and margins around the button.** Be mindful that the button title may vary in length depending on the locale.
> 최소 단추 크기와 단추 주변 여백을 유지하십시오. 단추 제목의 길이는 로케일에 따라 달라질 수 있습니다.
>




**NOTE**If the size you specify doesn’t accommodate the translated title for the type of payment button you’re using, the system automatically replaces it with the plain Apple Pay button shown below on the left. There is no automatic replacement for the Set up Apple Pay button.
> 참고 지정한 크기가 사용 중인 결제 버튼 유형에 대해 번역된 제목을 수용하지 않는 경우 시스템은 자동으로 왼쪽에 표시된 일반 Apple Pay 버튼으로 대체합니다. Apple Pay 설정 버튼을 자동으로 대체할 수 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay-Donate_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/Minimum-ApplePay-Donate_2x.png)

Use the following values for guidance.
> 지침으로 다음 값을 사용하십시오.
>




| Button | Minimum width | Minimum height | Minimum margins |
| --- | --- | --- | --- |
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Book with Apple PayBuy with Apple PayCheck out with Apple PayDonate with Apple PaySet up Apple PaySubscribe with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

# **Apple Pay mark**

Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other payment options in a similar manner. The Apple Pay mark is not a button; if you need an Apple Pay button, choose one of the buttons described in [Button types](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks#button-types). For design guidance related to showing Apple Pay as a payment option, see [Offering Apple Pay](../technologies/apple-pay/offering-apple-pay/).
> Apple Pay 마크 그래픽을 사용하여 다른 결제 옵션을 유사한 방식으로 표시할 때 Apple Pay가 사용 가능한 결제 옵션임을 표시합니다. Apple Pay 표시는 단추가 아닙니다. Apple Pay 단추가 필요한 경우 단추 유형에 설명된 단추 중 하나를 선택합니다. Apple Pay를 결제 옵션으로 표시하는 것과 관련된 설계 지침은 Apple Pay 제공을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayMarkWithPaymentOptions_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayMarkWithPaymentOptions_2x.png)

**Use only the artwork provided by Apple, with no alterations other than height.** You can specify a height for the Apple Pay mark, but make sure that the height you use is equal to or larger than other payment brand marks in your payment flow. Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t remove the border; don’t add visual effects to the mark, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the Apple Pay mark.
> Apple에서 제공하는 아트워크만 사용하십시오. 높이를 제외하고는 변경할 수 없습니다. Apple Pay 마크의 높이를 지정할 수 있지만, 사용하는 높이가 결제 흐름에서 다른 결제 브랜드 마크와 같거나 더 큰지 확인하십시오. 아트워크의 너비, 모서리 반지름 또는 가로 세로 비율을 조정하지 마십시오. 상표 기호나 다른 내용을 추가하지 마십시오. 테두리를 제거하지 마십시오. 그림자, 빛 또는 반사와 같은 시각적 효과를 마크에 추가하지 마십시오. Apple Pay 마크를 뒤집거나 회전하거나 애니메이션으로 만들지 마십시오.
>




**Maintain a minimum clear space around the mark of 1/10 of its height.** Don’t let the Apple Pay mark share its surrounding border with another graphic or button.
> Apple Pay 마크가 다른 그래픽이나 버튼과 주변 경계를 공유하지 않도록 높이의 10분의 1 정도의 최소 공백을 유지합니다.
>




Download the Apple Pay mark graphic and full usage guidelines [here](https://developer.apple.com/apple-pay/marketing/).
> 여기에서 Apple Paymark 그래픽과 전체 사용 지침을 다운로드하십시오.
>



