# **[technologies] tap-to-pay-on-iphone**

# Tap to Pay on iPhone lets merchants accept contactless payments using an enabled app on their iPhone, without having to connect external hardware.
> Tap to Pay on iPhone은 외부 하드웨어를 연결할 필요 없이 상인들이 아이폰에서 활성화된 앱을 사용하여 비접촉식 결제를 받을 수 있게 해준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-TapToPay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-TapToPay-intro_2x.png)

In addition to accepting in-person contactless payments, Tap to Pay on iPhone also lets merchants issue refunds, accept loyalty cards, and validate credit cards, such as when a customer wants to save their card for future use.
> Tap to Pay on iPhone은 고객이 미래에 사용하기 위해 카드를 저장하고 싶을 때와 같이 상인들이 환불을 하고, 로열티 카드를 받고, 신용카드를 확인할 수 있도록 해준다.
>




**NOTE**Tap to Pay on iPhone works alongside your existing payment acceptance hardware and accessories.
> 참고 iPhone에서 결제하는 탭은 기존 결제 승인 하드웨어 및 액세서리와 함께 작동합니다.
>




You can enable Tap to Pay on iPhone in an iOS app that you provide to merchants and businesses. Although a merchant’s customers don’t use your app directly, they view some of your app’s screens as they interact with the merchant, so it’s important to follow best practices for visual design and behavior. For high-level developer and business guidance, see [Tap to Pay on iPhone](https://developer.apple.com/tap-to-pay/).
> 당신은 당신이 가맹점과 기업에 제공하는 iOS 앱에서 아이폰에서 Tap to Pay를 활성화할 수 있다. 가맹점의 고객들은 당신의 앱을 직접 사용하지는 않지만, 그들이 가맹점과 상호 작용할 때 당신의 앱의 일부 화면을 보기 때문에 시각적 디자인과 행동에 대한 모범 사례를 따르는 것이 중요하다. 고급 개발자 및 비즈니스 지침은 아이폰에서 결제하기 탭을 참조하십시오.
>




# **Best practices**

**Make sure merchants accept Tap to Pay on iPhone terms and conditions before they begin a customer interaction.** Merchants must accept the terms and conditions before you perform the initial configuration on their devices, so it’s important that they do so before they begin a checkout or other customer-facing flow. For developer guidance, see [Configuring Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/configuring-tap-to-pay-on-iphone).
> 고객과의 상호 작용을 시작하기 전에 판매자가 iPhone 약관에 동의하는지 확인하십시오. 판매자는 장치에 초기 구성을 수행하기 전에 약관에 동의해야 하므로 체크아웃 또는 기타 고객 대면 흐름을 시작하기 전에 동의하는 것이 중요합니다. 개발자 지침은 iPhone에서 지불할 탭 구성을 참조하십시오.
>




**Present the Tap to Pay on iPhone terms and conditions to the appropriate business representative.** Specifically, if your app supports both administrator and nonadministrator accounts, be sure to present the terms and conditions to an administrator. If a nonadministrator tries to activate the feature, present a message explaining that administrator access is required.
> 아이폰 결제 탭을 해당 비즈니스 담당자에게 제시하십시오. 특히, 앱이 관리자 계정과 관리자가 아닌 계정을 모두 지원하는 경우 관리자에게 약관을 제시해야 합니다. 관리자가 아닌 사용자가 이 기능을 활성화하려고 하면 관리자 권한이 필요하다는 메시지를 표시합니다.
>




**Avoid making merchants wait to use Tap to Pay on iPhone.** In addition to performing the initial per-device configuration — which can take a few minutes — you need to perform a subsequent configuration each time your app becomes frontmost. You can minimize potential wait times by preparing the feature as soon as your app starts and immediately after each transition to the foreground. For developer guidance, see [prepare(using:)](https://developer.apple.com/documentation/proximityreader/paymentcardreader/prepare(using:)).
> 판매자가 iPhone에서 Tap to Pay를 사용할 때까지 기다리게 하지 마십시오. 초기 장치별 구성(몇 분 정도 걸릴 수 있음)을 수행하는 것 외에도 앱이 가장 앞에 나타날 때마다 후속 구성을 수행해야 합니다. 앱이 시작되자마자 그리고 포그라운드로 전환할 때마다 즉시 기능을 준비하여 잠재적인 대기 시간을 최소화할 수 있습니다. 개발자 지침은 준비(사용:)를 참조하십시오.
>




**Help merchants gauge how long a configuration is likely to take.** For example, consider displaying a [progress bar](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators#ios-ipados).
> 판매자가 구성에 소요될 가능성이 높은 시간을 측정할 수 있도록 도와줍니다. 예를 들어 진행률 표시줄을 표시하는 것을 고려해 보십시오.
>




**Consider helping merchants learn how to use Tap to Pay on iPhone before they interact with their customers.** For example, you could present screens that show how to accept payment from cards, digital wallets, and wearable devices like Apple Watch. You might want to display brief instructional content while the initial configuration step completes.
> 고객과 상호 작용하기 전에 상인들이 아이폰에서 탭 투 페이를 사용하는 방법을 배울 수 있도록 도와주는 것을 고려해 보십시오. 예를 들어, 당신은 카드, 디지털 지갑, 그리고 애플 워치와 같은 웨어러블 기기에서 결제를 받는 방법을 보여주는 화면을 제시할 수 있습니다. 초기 구성 단계가 완료되는 동안 간단한 지침 내용을 표시할 수 있습니다.
>




**Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support.** Because your support for Tap to Pay on iPhone is separate from your support for a hardware accessory like a Bluetooth chip and PIN reader, you can help merchants set up both payment acceptance solutions at the same time. After setup, make sure merchants can choose the appropriate solution during a checkout flow without having to visit your settings area to do so.
> 판매자가 iPhone의 Tap to Pay와 지원하는 하드웨어 액세서리 사이를 쉽게 전환할 수 있도록 합니다. iPhone의 Tap to Pay에 대한 지원은 Bluetooth 칩 및 PIN 판독기와 같은 하드웨어 액세서리에 대한 지원과는 별개이므로 판매자가 동시에 결제 승인 솔루션을 설정할 수 있도록 도울 수 있습니다. 설치 후에는 체크아웃 과정에서 소매업체가 설정 영역을 방문하지 않고도 적절한 솔루션을 선택할 수 있는지 확인하십시오.
>




# **Presentation**

Tap to Pay on iPhone is a payment acceptance method; it isn’t a payment method like Apple Pay, cash, or credit. It’s important for your app to present the feature correctly so that merchants can in turn represent it correctly to their customers.
> Tap to Pay on iPhone은 Apple Pay, 현금 또는 신용과 같은 결제 수단이 아닙니다. 앱이 기능을 올바르게 표시하여 판매자가 고객에게 올바르게 표시할 수 있도록 하는 것이 중요합니다.
>




During a Tap to Pay on iPhone experience, the system presents screens that help customers participate in the process. You need to supply information for the system to display in these screens, such as the merchant name and icon — available through the payment card reader token you receive from your payment service provider (PSP) — and the final transaction amount.
> Tap to Pay on iPhone을 사용하는 동안 시스템은 고객이 프로세스에 참여할 수 있도록 도와주는 화면을 제공합니다. PSP(결제 서비스 공급자)로부터 받은 결제 카드 판독기 토큰을 통해 사용할 수 있는 가맹점 이름 및 아이콘과 최종 거래 금액과 같은 시스템이 이러한 화면에 표시할 정보를 제공해야 합니다.
>




**Don’t confuse Apple Pay with Tap to Pay on iPhone.** Customers can use Tap to Pay on iPhone with Apple Pay, but it’s essential to distinguish the acceptance method from the payment method. In particular, avoid displaying an Apple Pay button near a Tap to Pay on iPhone button in your app.
> Apple Pay와 아이폰의 Tap to Pay를 혼동하지 마십시오. 고객은 Apple Pay와 함께 아이폰의 Tap to Pay를 사용할 수 있지만, 결제 방식과 결제 방식을 구분하는 것이 필수적입니다. 특히, 당신의 앱에서 iPhone의 Tap to Pay 버튼 근처에 Apple Pay 버튼이 표시되는 것을 피하세요.
>




**Make sure you know the final amount that customers need to pay before enabling the Tap to Pay on iPhone experience.** For example, if your app supports tipping or other customer interactions that can change the total, it’s important to ensure that merchants perform these interactions before they initiate Tap to Pay on iPhone. As much as possible, display the final amount customers need to pay in the Tap to Pay on iPhone screen.
> Tap to Pay on iPhone 경험을 활성화하기 전에 고객이 최종적으로 지불해야 하는 금액을 알고 있는지 확인하십시오. 예를 들어, 앱에서 팁을 주거나 전체를 변경할 수 있는 다른 고객 상호 작용을 지원하는 경우, 판매자가 Tap to Pay on iPhone을 시작하기 전에 이러한 상호 작용을 수행하는지 확인하는 것이 중요합니다. 고객이 지불해야 하는 최종 금액을 아이폰의 Tap to Pay 화면에 최대한 표시합니다.
>




**If your app supports multiple payment acceptance methods, make the Tap to Pay on iPhone button easy to find.** As much as possible, avoid making merchants scroll to access the feature. If your app doesn’t support other payment acceptance options, you can open Tap to Pay on iPhone automatically when checkout begins.
> 앱에서 여러 결제 승인 방법을 지원하는 경우 아이폰에서 결제 탭 버튼을 쉽게 찾을 수 있도록 하십시오. 가능한 한 가맹점이 해당 기능에 액세스하도록 스크롤하지 마십시오. 앱이 다른 결제 승인 옵션을 지원하지 않는 경우, 체크아웃이 시작될 때 자동으로 아이폰에서 결제 탭을 열 수 있습니다.
>




**For the button that activates the feature, prefer the label “Tap to Pay on iPhone” or — if space is constrained — “Tap to Pay.”** Alternatively, if you use icons in buttons that enable other acceptance methods, use the `wave.3.right.circle` or `wave.3.right.circle.fill` [symbol](../foundations/sf-symbols) in your Tap to Pay on iPhone button. Regardless of which design you choose, be sure to avoid including the Apple logo.
> 기능을 활성화하는 단추의 경우 "iPhone에서 결제하려면 탭" 또는 공간이 제한된 경우 "결제하려면 탭" 레이블을 사용합니다. 또는 다른 허용 방법을 사용하는 단추에 아이콘을 사용하는 경우에는 "wave.3.right.circle" 또는 "wave.3.right.circle"을 사용합니다.iPhone에서 지불하기 탭 버튼의 기호를 채웁니다. 어떤 디자인을 선택하든 Apple 로고를 포함하지 않도록 하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-symbol-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-symbol-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-logo-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-logo-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

If Tap to Pay on iPhone is the only payment acceptance method you support, you can re-use existing “Charge” or “Checkout” buttons to activate Tap to Pay on iPhone, if necessary.
> 지원하는 결제 승인 방법이 아이폰에서 탭 투 페이뿐이라면, 필요한 경우 기존의 '충전' 또는 '체크아웃' 버튼을 다시 사용하여 아이폰에서 탭 투 페이를 활성화할 수 있습니다.
>




# **Additional interactions**

To support situations like looking up a past transaction or retaining card information to ensure future payment, Tap to Pay on iPhone lets merchants read a payment card when there’s no transaction amount.
> 과거 거래를 조회하거나 향후 결제를 보장하기 위해 카드 정보를 보관하는 등의 상황을 지원하기 위해, 아이폰에서 탭 투 페이는 거래 금액이 없을 때 가맹점이 결제 카드를 읽을 수 있도록 한다.
>




When people have other types of NFC-enabled cards or passes in Apple Wallet — such as loyalty, discount, and points cards — Tap to Pay on iPhone lets merchants read these items at the same time as they read a payment card or independently.
> 사람들이 로열티, 할인 및 포인트 카드와 같은 다른 유형의 근거리 무선 통신 가능 카드를 가지고 있거나 Apple Wallet에서 패스를 받을 때, 아이폰에서 탭 투 페이는 상인들이 결제 카드를 읽는 동시에 또는 독립적으로 이러한 항목을 읽을 수 있게 한다.
>




**If you support an independent loyalty card transaction, distinguish this flow from a payment acceptance flow that uses Tap to Pay on iPhone.** For example, give merchants a separate button to initiate a loyalty card transaction, using a button label that helps them avoid choosing the wrong one by mistake.
> 독립적인 로열티 카드 거래를 지원하는 경우 이 흐름을 iPhone에서 Tap to Pay를 사용하는 결제 승인 흐름과 구분하십시오. 예를 들어 가맹점이 실수로 잘못 선택하지 않도록 도와주는 버튼 레이블을 사용하여 로열티 카드 거래를 시작할 수 있는 별도의 버튼을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/loyalty-card_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/loyalty-card_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-loyalty_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-loyalty_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-payment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-payment_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)
