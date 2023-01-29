# **[technologies] in-app-purchase**

# People can use in-app purchase to pay for virtual goods — like premium content, digital goods, and subscriptions — securely within your app, regardless of the device on which it runs.
> 사람들은 앱 내에서 구매한 프리미엄 콘텐츠, 디지털 상품 및 구독과 같은 가상 상품을 앱이 실행되는 장치에 관계없이 안전하게 결제할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-IAP-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-IAP-intro_2x.png)

You can also promote and offer in-app purchases directly through the App Store. For developer guidance, see [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app_purchase).
> 앱스토어를 통해 앱 내 구매를 직접 홍보하고 제공할 수도 있다. 개발자 지침은 앱 내 구매를 참조하십시오.
>




**IMPORTANT**In-app purchase and [Apple Pay](../technologies/apple-pay/introduction) are different technologies that support different use cases. Use in-app purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.
> 중요 앱 내 구매와 Apple Pay는 서로 다른 사용 사례를 지원하는 서로 다른 기술입니다. 앱 내 구매를 통해 앱의 프리미엄 콘텐츠 및 디지털 콘텐츠 구독과 같은 가상 상품을 판매할 수 있습니다. Apple Pay를 사용하여 식료품, 의류 및 가전제품과 같은 실물 상품을 판매하고, 클럽 회원권, 호텔 예약, 이벤트 티켓과 같은 서비스를 판매하고, 기부를 할 수 있습니다.
>




Using in-app purchase, there are four types of content you can offer:
> 앱 내 구매를 사용하여 제공할 수 있는 콘텐츠는 4가지 유형이 있습니다:
>




- *Consumable* content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.
- >  게임에서 생명이나 보석과 같은 소모성 콘텐츠. 구매 후 소모성 콘텐츠는 사람들이 사용함에 따라 고갈되고, 사람들은 그것을 다시 구매할 수 있다.

- *Non-consumable* content like premium features in an app. Purchased non-consumable content doesn’t expire.
- >  앱의 프리미엄 기능과 같은 비소모 콘텐츠. 구입한 비소모 콘텐츠는 만료되지 않습니다.

- *Auto-renewable subscriptions* to virtual content, services, and premium features in your app on an ongoing basis. An auto-renewable subscription continues to automatically renew at the end of each subscription period until people choose to cancel it.
- >  앱의 가상 콘텐츠, 서비스 및 프리미엄 기능에 대한 구독을 지속적으로 자동 갱신할 수 있습니다. 자동 갱신 구독은 사용자가 취소를 선택할 때까지 각 구독 기간이 끝날 때마다 자동으로 갱신됩니다.

- *Non-renewing subscriptions* to a service or content that lasts for a limited time, like access to an in-game battle pass. People purchase a non-renewing subscription each time they want to extend their access to the service or content.
- >  게임 내 배틀 패스에 대한 액세스와 같이 제한된 시간 동안 지속되는 서비스 또는 콘텐츠에 대한 비갱신 구독입니다. 사용자는 서비스 또는 콘텐츠에 대한 액세스 권한을 확장할 때마다 갱신되지 않는 구독을 구입합니다.


![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iap-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iap-intro_2x.png)

For marketing and business guidance, see [In-app purchase](https://developer.apple.com/in-app-purchase/) and [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/). For information about what you can and can’t sell in your app, including in-app purchase usage requirements and restrictions, see [App Store review guidelines](https://developer.apple.com/app-store/review/guidelines/).
> 마케팅 및 비즈니스 지침은 앱 내 구매 및 자동 갱신 구독을 참조하십시오. 앱 내 구매 사용 요구 사항 및 제한 사항을 포함하여 앱에서 판매할 수 있는 것과 판매할 수 없는 것에 대한 자세한 내용은 앱 스토어 검토 지침을 참조하십시오.
>




# **Best practices**

**Let people experience your app before making a purchase.** People may be more inclined to invest in paid items or features after they’ve enjoyed your app and discovered its value. If you offer auto-renewable subscriptions, consider supporting limited free access to your content; for guidance, see [Auto-renewable subscriptions](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#auto-renewable-subscriptions).
> 사람들이 당신의 앱을 구매하기 전에 경험하도록 하라. 사람들은 당신의 앱을 즐기고 그 가치를 발견한 후에 유료 아이템이나 기능에 더 투자하는 경향이 있을 수 있다. 자동 갱신 구독을 제공하는 경우 콘텐츠에 대한 제한된 무료 액세스 지원을 고려하십시오. 자세한 내용은 자동 갱신 구독을 참조하십시오.
>




**Design an integrated shopping experience.** You don’t want people to think they’ve entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.
> 통합된 쇼핑 환경을 설계하십시오. 디지털 제품을 탐색하고 구입할 때 다른 앱을 입력했다고 생각하지 않도록 해야 합니다. 앱 스타일을 반영하는 방식으로 제품을 제시하고 트랜잭션을 처리합니다.
>




**Use simple, succinct product names and descriptions.** Titles that don’t truncate or wrap and plain, direct language can help people find products quickly.
> 간결하고 간결한 제품 이름과 설명을 사용하십시오. 잘라내거나 싸지 않는 제목과 평이하고 직접적인 언어를 사용하면 제품을 빠르게 찾을 수 있습니다.
>




**Display the total billing price for each in-app purchase you offer, regardless of type.** People need to know the total billing amount for every purchase they consider.
> 제공하는 각 인앱 구매에 대한 총 청구 금액을 종류에 관계없이 표시합니다. 사람들은 그들이 고려하는 모든 구매에 대한 총 청구 금액을 알아야 합니다.
>




**Display your store only when people can make payments.** If someone canʼt make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isnʼt available. For developer guidance, see [AppStore.canMakePayments](https://developer.apple.com/documentation/storekit/appstore/3822277-canmakepayments).
> 부모의 제한 등으로 인해 결제할 수 없는 경우 상점을 숨기거나 상점을 사용할 수 없는 이유를 설명하는 UI를 표시하는 것이 좋습니다. 개발자 지침은 AppStore.canMakePayments를 참조하십시오.
>




**Use the default confirmation sheet.** When someone initiates an in-app purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don’t modify or replicate this sheet.
> 기본 확인 시트를 사용하십시오. 앱 내 구매를 시작하면 시스템에 확인 시트가 표시되어 우발적인 구매를 방지할 수 있습니다. 이 시트를 수정하거나 복제하지 마십시오.
>




# **Enabling Family Sharing**

People can use Family Sharing to share access to their purchased content — such as auto-renewable subscriptions and non-consumable in-app purchases — with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.
> 가족 공유를 사용하면 자동 갱신 구독 및 앱 내 비소모 구매와 같은 구입한 콘텐츠에 대한 액세스를 최대 5명의 추가 가족 구성원과 모든 Apple 장치에서 공유할 수 있습니다. 사용자가 제공하는 가족 공유 지원을 사람들이 이용하도록 권장하려면 다음 지침을 고려하십시오.
>




**Prominently mention Family Sharing in places where people learn about the content you offer.** For example, including “Family” or “Shareable” in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.
> 사용자가 제공하는 콘텐츠에 대해 사람들이 배우는 장소에서 가족 공유를 눈에 띄게 언급하십시오. 예를 들어 구독 또는 항목 이름에 "가족" 또는 "공유 가능"을 포함하고 가입 화면에서 가족 공유를 참조하면 기능을 강조하고 정보에 입각한 선택을 할 수 있습니다.
>




**Help people understand the benefits of Family Sharing and how to participate.** When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings. For example, an existing subscriber whose sharing setting is turned off (the default) receives a notice from Apple that invites them to share their subscription with family members. Similarly, a family member can get a notification about content that’s being shared with them. (To learn more about the types of notifications people can receive, see [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/).)
> 가족 공유의 이점과 참여 방법을 사람들이 이해할 수 있도록 도와줍니다. 가족 공유를 설정하면 현재 설정에 따라 변경 내용에 대한 알림을 받을 수 있습니다. 예를 들어, 공유 설정이 해제된 기존 가입자(기본값)는 Apple로부터 가족 구성원과 구독을 공유하도록 초대하는 통지를 받습니다. 마찬가지로 가족 구성원은 자신과 공유 중인 콘텐츠에 대한 알림을 받을 수 있습니다
>




**Aim to customize your in-app messaging so that it makes sense to both purchasers and family members.** For example, when a family member views shared content for the first time, you might welcome them with wording like “Your family subscription includes...”
> 가족 구성원이 공유 콘텐츠를 처음 볼 때 "가족 가입에 포함됩니다..."와 같은 문구로 환영할 수 있습니다
>




# **Providing help with in-app purchases**
> 앱 내 구매에 대한 도움말 제공
>




Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow. For developer guidance, see [beginRefundRequest(for:in:)](https://developer.apple.com/documentation/storekit/transaction/3803219-beginrefundrequest); for related guidance specific to auto-renewable subscriptions, see [Helping people manage their subscriptions](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#helping-people-manage-their-subscriptions).
> 때때로, 사람들은 구매에 도움이 필요하거나 환불을 요청하기를 원한다. 이러한 경험을 편리하게 하기 위해 지원을 제공하고 대체 솔루션을 제공하며 사람들이 시스템에서 제공하는 환불 흐름을 시작하도록 돕는 사용자 지정 UI를 앱 내에 제공할 수 있습니다. 개발자 지침은 환불 요청 시작(:in:)을 참조하십시오. 자동 갱신 구독과 관련된 관련 지침은 사용자의 구독 관리 지원을 참조하십시오.
>




**Provide help that customers can view before they request a refund.** In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app. For example, your custom screen might help people resolve problems with missing purchases, answer frequently asked questions about the in-app purchases you offer, and give people ways to submit feedback or contact you directly for support.
> 고객이 환불을 요청하기 전에 볼 수 있는 도움말을 제공합니다. 시스템에서 제공하는 환불 흐름에 대한 링크를 포함하는 것 외에도 사용자 지정 구매 도움말 화면은 사용자가 앱에 맞게 조정할 수 있는 지원을 제공합니다. 예를 들어, 사용자 지정 화면을 사용하면 누락된 구매와 관련된 문제를 해결하고, 제공하는 앱 내 구매에 대해 자주 묻는 질문에 답변하며, 피드백을 제출하거나 지원을 위해 사용자에게 직접 연락할 수 있는 방법을 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/custom-purchase-help_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/custom-purchase-help_2x.png)

**Use a simple title for the refund action, like “Refund” or “Request a Refund”.** The system-provided refund flow makes it clear that people request a refund from Apple, so there’s no need to reiterate this information.
> 환불 조치에는 "환불" 또는 "환불 요청"과 같은 간단한 제목을 사용하십시오. 시스템에서 제공하는 환불 흐름은 사람들이 Apple에 환불을 요청한다는 것을 명확하게 하므로 이 정보를 반복할 필요가 없습니다.
>




**Help people find the problematic purchase.** For each recent purchase you display, include contextual information that helps people identify the one they want. For example, you might display an image of the product — along with its name and description — and list the original purchase date.
> 사용자가 문제가 있는 구매를 찾을 수 있도록 도와줍니다. 표시하는 각 최근 구매에 대해 사용자가 원하는 구매를 식별하는 데 도움이 되는 상황별 정보를 포함합니다. 예를 들어 제품의 이름 및 설명과 함께 제품 이미지를 표시하고 원래 구매 날짜를 나열할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/custom-refund-request_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/custom-refund-request_2x.png)

**Consider offering alternative solutions.** For example, if the customer didn’t receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.
> 다른 해결책을 제시하는 것을 고려해 보십시오. 예를 들어, 고객이 구입한 제품을 받지 못한 경우 즉시 이행하거나 유화적인 제품을 제안할 수 있습니다. 당신이 제공하는 대안에 상관없이, 사람들이 여전히 환불을 요청할 수 있다는 것을 분명히 하세요.
>




**Make it easy for people to request a refund.** Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal your refund-request button. When people choose your refund-request item, they automatically enter the system-provided refund flow shown below.
> 사용자가 쉽게 환불을 요청할 수 있도록 하십시오. 구매 도움말 화면에서 유용한 정보와 대체 솔루션을 제공할 수 있지만 이 콘텐츠가 환불을 요청하는 데 장애가 되지 않도록 하십시오. 예를 들어, 사용자가 다른 화면을 스크롤하거나 열어 환불 요청 버튼을 표시하지 않도록 합니다. 사용자가 환불 요청 항목을 선택할 때 아래에 표시된 시스템에서 제공하는 환불 흐름을 자동으로 입력합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-refund-flow-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-refund-flow-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-refund-flow-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-refund-flow-2_2x.png)

**Avoid characterizing or providing guidance on Apple’s refund policies.** For example, don’t speculate about whether customers will receive the refund they request. To help people understand the refund-request process, you can provide a link to [Request a refund for apps or content that you bought from Apple](https://support.apple.com/en-us/HT204084).
> Apple의 환불 정책에 대해 설명하거나 지침을 제공하는 것을 피하십시오. 예를 들어, 고객이 요청한 환불을 받을지 여부에 대해 추측하지 마십시오. 환불 요청 프로세스를 쉽게 이해할 수 있도록 Apple에서 구입한 앱 또는 콘텐츠에 대한 환불 요청 링크를 제공할 수 있습니다.
>




# **Auto-renewable subscriptions**

**Highlight subscription benefits during onboarding.** By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain by subscribing. Include a strong call to action and a clear summary of subscription terms (see [Making signup effortless](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#making-signup-effortless)). For related guidance, see [Onboarding](../patterns/onboarding).
> 온보딩 중에 구독 혜택을 강조합니다. 사람들이 앱을 처음 시작할 때 구독의 가치를 보여줌으로써 앱의 작동 방식을 교육하고 구독을 통해 얻을 수 있는 이점을 이해하도록 도울 수 있습니다. 강력한 영업 활용 방안과 구독 조건에 대한 명확한 요약을 포함합니다(쉽지 않은 등록 참조). 관련 지침은 온보드를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-onboarding_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-onboarding_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-onboarding_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-onboarding_2x.png)

**Offer a range of content choices, service levels, and durations.** People appreciate the flexibility to choose the subscription that best meets their needs.
> 다양한 컨텐츠 선택, 서비스 수준 및 기간을 제공합니다. 사람들은 자신의 요구에 가장 적합한 구독을 선택할 수 있는 유연성을 높이 평가합니다.
>




**Consider letting people try your content for free before signing up.** Limited free access gives people the opportunity to sample your content and encourages engaged users to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.
> 사용자가 등록하기 전에 사용자의 콘텐츠를 무료로 사용할 수 있도록 허용하는 것을 고려하십시오. 제한된 무료 액세스 권한은 사용자에게 사용자의 콘텐츠를 샘플링할 수 있는 기회를 제공하고 사용자가 등록하도록 장려합니다. 예를 들어, 무료 앱, 미터기 요금제 또는 무료 평가판을 제공할 수 있습니다.
>




• [Freemium app](../technologies/in-app-purchase#)
• [Metered paywall](../technologies/in-app-purchase#)
• [Free trial](../technologies/in-app-purchase#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/freemium-app_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/freemium-app_2x.png)


**Prompt people to subscribe at relevant times, like when they near their monthly limit of free content.** Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.
> 매월 무료 콘텐츠 한도에 근접했을 때와 같이 사용자가 관련 시간에 구독하도록 유도합니다. 또한 앱 전체의 관련 지점에 프롬프트를 포함하여 사용자가 언제든지 쉽게 구독할 수 있도록 하십시오.
>




**Encourage a new subscription only when someone isn’t already a subscriber.** Otherwise, people may believe their existing subscription has lapsed when that’s not actually the case. If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think they have to pay multiple times for the same service.
> 다른 사용자가 아직 가입자가 아닌 경우에만 새 가입을 권장합니다. 그렇지 않은 경우에는 기존 가입이 만료되었다고 생각할 수 있습니다. 여러 앱에서 또는 웹 사이트를 통해 동일한 구독 옵션을 제공하는 경우, 사람들이 동일한 서비스에 대해 여러 번 비용을 지불해야 한다고 생각하지 않도록 로그인 옵션을 제공하십시오.
>




# **Making signup effortless**

A simple and informative sign-up experience makes it easy for people to act on their interest in your content, whether they’re in your app or viewing your App Store product page.
> 간단하고 유익한 등록 환경을 통해 사용자가 앱에 있든, 앱 스토어 제품 페이지를 보든 관계없이 사용자의 콘텐츠에 대한 관심에 따라 쉽게 작업할 수 있습니다.
>




**Provide clear, distinguishable subscription options.** Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.
> 명확하고 구별 가능한 구독 옵션을 제공합니다. 구독 옵션을 서로 구별하는 짧은 자체 설명 이름을 사용하고 각 옵션의 가격과 기간을 지정하십시오. 소개 가격을 제시할 경우, 소개 가격, 제안 기간 및 제안이 종료된 후 고객이 지불하는 표준 가격을 반드시 기재하십시오.
>




**Simplify initial signup by asking only for necessary information.** A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.
> 필요한 정보만 요청하여 초기 가입을 간소화하십시오. 가입 절차가 길어지면 가입 전환율이 낮아질 수 있습니다. 사용자가 등록할 때까지 추가 정보 요청을 연기합니다.
>




**In your tvOS app, help people sign up or authenticate using another device.** Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.
> 사용자의 TVOS 앱에서 다른 장치를 사용하여 사용자가 등록하거나 인증할 수 있도록 도와줍니다. 사용자의 TVOS 앱에 정보를 입력하도록 요청하는 대신 필요한 정보를 입력할 수 있는 다른 장치로 코드를 보냅니다.
>




**Give people more information in your app’s sign-up screen.** In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include:
> 앱 등록 화면에서 사용자에게 더 많은 정보를 제공합니다. 앱 및 앱 스토어 메타데이터에 서비스 약관 및 개인 정보 보호 정책에 대한 링크를 포함하는 것 외에도, 앱 내 등록 화면에는 다음이 포함되어야 합니다:
>




- The subscription name, duration, and the content or services provided during each subscription period
- >  구독 이름, 기간 및 각 구독 기간 동안 제공된 콘텐츠 또는 서비스

- The billing amount, correctly localized for the territories and currencies where the subscription is available for purchase
- >  구독을 구입할 수 있는 지역 및 통화에 대해 올바르게 현지화된 청구 금액

- A way for existing subscribers to sign in or restore purchases
- >  기존 가입자가 로그인하거나 구매를 복원하는 방법


For example, the Forest Explorer sign-up screen displays billing totals for monthly, biannual, and annual subscriptions in the most prominent positions. In subordinate positions, it shows breakdowns of the biannual and annual prices, so that people can compare the values and make an informed choice. The sign-up screen also contains a button that existing subscribers can use to restore their purchases.
> 예를 들어 Forest Explorer 가입 화면에는 월별, 반기별 및 연간 구독에 대한 청구 총액이 가장 눈에 띄는 위치에 표시됩니다. 하위직에서는, 그것은 사람들이 가치를 비교하고 정보에 입각한 선택을 할 수 있도록 2년에 한 번 있는 가격과 연간 가격의 내역을 보여준다. 가입 화면에는 기존 가입자가 구매를 복원하는 데 사용할 수 있는 버튼도 포함돼 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-upgrade_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-upgrade_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-upgrade_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-upgrade_2x.png)

**Clearly describe how a free trial works.** It’s particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period. For example, the Ocean Journal sign-up screen explicitly states both the duration of the free trial and the amount that’s billed when it ends.
> 무료 평가판의 작동 방식을 명확히 설명하십시오. 무료 평가판이 끝나면 다음 구독 기간 동안 자동으로 결제가 시작된다는 사실을 사람들에게 알리는 것이 특히 중요합니다. 예를 들어 Ocean Journal 가입 화면에는 무료 평가판의 기간과 평가판이 종료될 때 청구되는 금액이 명시적으로 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-free-trial_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/iphone-free-trial_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-free-trial_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/watch-free-trial_2x.png)

**Include a sign-up opportunity in your app’s settings.** App and account settings are common places for people to look for a way to subscribe.
> 앱 설정에 가입 기회를 포함하십시오. 앱과 계정 설정은 사람들이 구독 방법을 찾기 위한 일반적인 장소입니다.
>




# **Supporting offer codes**

Subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content. For example, you might provide offer codes through email, give them out at a store or event, or print one on a physical product.
> 구독 제안 코드를 사용하면 온라인 및 오프라인 채널을 모두 사용하여 새, 기존 및 만료된 구독자에게 구독 콘텐츠에 대한 무료 또는 할인된 액세스 권한을 부여할 수 있습니다. 예를 들어 이메일을 통해 오퍼 코드를 제공하거나 상점 또는 이벤트에서 코드를 배포하거나 실제 제품에 코드를 인쇄할 수 있습니다.
>




There are two types of offer codes you can support:
> 지원할 수 있는 오퍼 코드에는 두 가지 유형이 있습니다:
>




- A *one-time use code* is a unique code you generate in App Store Connect. People can redeem a one-time use code on a website, within your app (when you support redemption), or by entering it in the App Store, where they’re prompted to install your app if they haven’t already. Consider using one-time use codes when your distribution is small or when you need to restrict access to a code.
- >  일회용 코드는 App Store Connect에서 생성하는 고유 코드입니다. 사용자는 웹 사이트, 앱 내에서(사용자가 상환을 지원할 때) 또는 앱 스토어에 1회용 코드를 입력하여 아직 설치하지 않은 경우 앱을 설치하라는 메시지를 표시할 수 있습니다. 분포가 작거나 코드에 대한 액세스를 제한해야 할 때 일회성 사용 코드를 사용하는 것을 고려하십시오.

- A *custom code* is a code you create, such as NEWYEAR or SPRINGSALE. People can redeem a custom code on a website or within your app (when you support redemption). Consider using a custom code when you want to support a large campaign that requires a mass distribution of codes.
- >  사용자 지정 코드는 NEW YEAR 또는 SpringSale과 같은 사용자가 만든 코드입니다. 사용자 지정 코드는 웹 사이트 또는 앱에서 사용자 지정 코드를 사용할 수 있습니다(사용자 지정 코드를 사용자가 사용자 지정 코드를 지원할 때). 코드를 대량으로 배포해야 하는 대규모 캠페인을 지원하려면 사용자 지정 코드를 사용하는 것을 고려하십시오.


For technical details and business guidance on using both types of offer codes, see [Offer codes](https://developer.apple.com/app-store/subscriptions/#offer-codes); to learn more about other types of offers, see [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).
> 두 가지 유형의 오퍼 코드 사용에 대한 기술 세부 정보 및 비즈니스 지침은 오퍼 코드를 참조하십시오. 다른 유형의 오퍼에 대한 자세한 내용은 서브스크립션 오퍼 제공을 참조하십시오.
>




**Clearly explain offer details.** To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.
> 제안 세부사항을 명확하게 설명하십시오. 사람들이 정보에 입각한 결정을 내리도록 돕기 위해 마케팅 자료에 제안에 대한 간단명료한 설명을 제공하십시오.
>




**Follow guidelines for creating a custom code.** A custom code can contain only alphanumeric ASCII characters. Don’t use special characters, including Chinese and Arabic characters.
> 사용자 지정 코드를 만들려면 지침을 따르십시오. 사용자 지정 코드에는 영숫자 ASCII 문자만 포함될 수 있습니다. 한자와 아랍 문자를 포함한 특수 문자를 사용하지 마십시오.
>




**Tell people how to redeem a custom code.** Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it on your website or within your app.
> 사용자 지정 코드를 사용하는 방법을 알려줍니다. 앱스토어 계정 설정에 입력하여 사용자 지정 코드를 사용할 수 없기 때문에 웹 사이트나 앱에서 사용자 지정 코드를 사용할 수 있음을 알리는 것이 중요합니다.
>




**Consider supporting offer redemption within your app.** The system automatically provides screens that enable the offer-redemption flow, whether people redeem the offer in your app or in the App Store. When you use StoreKit API to let people redeem offer codes within your app, the only custom UI you need to create is one that initiates the system-provided flow (for developer guidance, see [presentCodeRedemptionSheet](https://developer.apple.com/documentation/storekit/skpaymentqueue/3566726-presentcoderedemptionsheet)). There are several natural places to provide this custom UI. For example, you could add a “Redeem Code” button to your paywall, onboarding screens, or your app’s settings screen.
> 앱 내에서 오퍼 상환을 지원하는 것을 고려해 보십시오. 시스템은 자동으로 오퍼 상환 흐름을 가능하게 하는 화면을 제공합니다. 사람들이 당신의 앱에서 또는 앱 스토어에서 오퍼를 상환하는지 여부에 관계없이. StoreKit API를 사용하여 사람들이 앱 내에서 오퍼 코드를 상환할 수 있도록 할 때, 시스템에서 제공하는 흐름을 시작하는 사용자 지정 UI만 생성하면 됩니다(개발자 지침은 현재 코드 상환 참조)시트). 이 사용자 지정 UI를 제공할 수 있는 몇 가지 자연스러운 장소가 있습니다. 예를 들어, 당신은 당신의 페이월, 탑승 화면 또는 당신의 앱의 설정 화면에 "코드 상환" 버튼을 추가할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/redeem-button-on-free-trial_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/redeem-button-on-free-trial_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/subscription-management_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/subscription-management_2x.png)

After people tap your custom redeem button, the system automatically provides a series of code-redemption screens like the ones shown below.
> 사용자가 사용자 정의 상환 버튼을 누르면 시스템은 아래와 같은 일련의 코드 상환 화면을 자동으로 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-3_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-provided-redemption-3_2x.png)

**Supply an engaging and informative promotional image.** Creating this optional image can help people understand the value of your content. If you don’t supply a promotional image, the code redemption screens use your app icon by default. To learn more, see [Promoting your in-app purchases](https://developer.apple.com/app-store/promoting-in-app-purchases/).
> 매력적이고 유익한 홍보 이미지를 제공하십시오. 이 선택적 이미지를 만들면 사람들이 콘텐츠의 가치를 이해하는 데 도움이 될 수 있습니다. 만약 당신이 홍보 이미지를 제공하지 않는다면, 코드 상환 화면은 기본적으로 당신의 앱 아이콘을 사용한다. 자세한 내용은 앱 내 구매 촉진을 참조하십시오.
>




**Help people benefit from unlocked content as soon as they complete the redemption flow.**Think about ways to align the post-redemption experience in your app with the subscriber’s new status. For example, you might provide a welcome experience for new subscribers or a brief tour of new features for an existing subscriber who’s unlocked additional functionality. In particular, be prepared to welcome people who subscribe before they open your app for the first time. For example, if you require people to create an account or sign in before they can use your app, make this process as smooth as possible for new subscribers who haven’t experienced it before.
> 사용자가 상환 흐름을 완료하는 즉시 잠금 해제된 콘텐츠의 이점을 누릴 수 있도록 지원합니다.당신의 앱에서 상환 후 경험을 가입자의 새로운 상태에 맞추는 방법을 생각해보세요. 예를 들어, 새 가입자에게 환영 인사를 하거나 추가 기능을 잠금 해제한 기존 가입자에게 새 기능에 대한 간단한 둘러보기를 제공할 수 있습니다. 특히, 앱을 처음 열기 전에 구독하는 사람들을 환영할 준비를 하세요. 예를 들어, 사용자가 앱을 사용하기 전에 계정을 만들거나 로그인하도록 요구하는 경우 이전에 이를 경험하지 않은 신규 가입자를 위해 이 프로세스를 최대한 부드럽게 만드십시오.
>




# **Helping people manage their subscriptions**
> 사용자의 헤드라인 등록 관리 지원
>




Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.
> 구독 관리를 지원한다는 것은 사용자가 앱을 떠나지 않고도 구독을 업그레이드, 다운그레이드 또는 취소할 수 있다는 것을 의미합니다. 또한 앱 내에서 구독 관리를 제공하면 일반적인 구독자 문제에 대한 도움말을 제공하고 사람들이 고려할 수 있는 대안을 제시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/subscription-management_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/subscription-management_2x.png)

**Provide summaries of the customer’s subscriptions.** In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option. For developer guidance, see [Product.SubscriptionInfo](https://developer.apple.com/documentation/storekit/product/subscriptioninfo).
> 고객의 구독 요약을 제공합니다. 특히, 사람들은 검색할 필요 없이 다가오는 갱신 날짜를 보는 것을 좋아합니다. 구독 관리 옵션 근처의 설정 또는 계정 화면에 이 정보를 표시하는 것이 좋습니다. 개발자 지침은 제품을 참조하십시오.구독 정보.
>




**Consider using the system-provided subscription-management UI.** Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app. For developer guidance, see [showManageSubscriptions(in:)](https://developer.apple.com/documentation/storekit/appstore/3803198-showmanagesubscriptions).
> 시스템에서 제공하는 구독 관리 UI를 사용해 보십시오. StoreKit API를 사용하면 사용자가 앱을 떠나지 않고도 구독을 관리하거나 취소할 수 있는 일관된 환경을 제공할 수 있습니다. 개발자 지침은 showManageSubscriptions(가입 관리)(in:)를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-cancel-flow-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-cancel-flow-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-cancel-flow-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/system-cancel-flow-2_2x.png)

**Consider ways to encourage a subscriber to keep their subscription or resubscribe later.**When you use StoreKit APIs, your app is notified when someone chooses to cancel their subscription. In this scenario, you might want to extend a personalized offer as an alternative to cancellation or invite people to describe their reasons for canceling in an exit survey. In addition to giving you insights into various customer problems, survey feedback can also help inform messaging for retention and win-back strategies.
> 가입자가 구독을 유지하거나 나중에 다시 구독하도록 권장하는 방법을 고려하십시오.StoreKit API를 사용할 때 누군가가 구독을 취소하기로 선택하면 앱에 알림이 표시됩니다. 이 시나리오에서는 취소의 대안으로 개인화된 제안을 확장하거나 출구 조사에서 취소 이유를 설명하도록 사람들을 초대할 수 있습니다. 설문 조사 피드백을 통해 다양한 고객 문제에 대한 통찰력을 얻을 수 있을 뿐만 아니라 유지 및 복구 전략에 대한 메시지를 제공할 수도 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/promotional-offer_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/promotional-offer_2x.png)

**Always make it easy for customers to cancel an auto-renewable subscription.** If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling.
> 항상 고객이 자동 갱신 구독을 쉽게 취소할 수 있도록 하십시오. 구독 관리 작업이 앱 내에 있거나 인식하기 어려운 경우 구독자는 자신이 취소하는 것을 막거나 방해받고 있다고 느낄 수 있습니다.
>




**Consider creating a branded, contextual experience to complement the system-provided management UI.** Within your custom UI, you might offer a popular premium tier or provide personalized suggestions for alternative plans based on what you know about the customer’s preferences or how they use your app. For example, you can create a promotional offer that provides a discounted price for a specific period of time. You might also consider subscription [offer codes](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#supporting-offer-codes) to help you win back lapsed subscribers and encourage existing subscribers to upgrade.
> 시스템에서 제공하는 관리 UI를 보완하기 위해 브랜드 환경을 구축하는 것을 고려해 보십시오. 사용자 지정 UI 내에서 고객의 선호도나 앱 사용 방법에 대해 알고 있는 내용에 따라 인기 있는 프리미엄 계층을 제공하거나 대체 요금제에 대한 맞춤형 제안을 제공할 수 있습니다. 예를 들어, 특정 기간 동안 할인된 가격을 제공하는 판촉 행사를 만들 수 있습니다. 만료된 구독자를 되찾고 기존 구독자의 업그레이드를 장려하기 위해 구독 제안 코드를 고려할 수도 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항은 없습니다.
>




# **watchOS**

The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. For the complete list of required items, see [Making signup effortless](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#making-signup-effortless). The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.
> 시계의 가입 화면OS 앱은 다른 버전의 앱에 표시하는 것과 동일한 구독 옵션 정보 집합을 표시해야 합니다. 필수 항목의 전체 목록은 쉽게 등록하기를 참조하십시오. 다음 지침은 Apple Watch에서 편안한 느낌의 등록 화면을 설계하는 데 도움이 될 수 있습니다.
>




**Clearly describe the differences between versions of your app that run on different devices.**If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing subscription content through your watchOS app without implying that the experience is identical to the ones in other versions of your app.
> 다른 장치에서 실행되는 앱 버전 간의 차이를 명확히 설명하십시오.네 시계라면OS 앱은 다른 기능을 지원하거나 다른 장치에서 사용할 수 있는 콘텐츠의 하위 집합을 제공하므로 설명에서 이러한 차이점을 명확히 해야 합니다. 시계를 통해 구독 컨텐츠에 액세스할 때의 이점을 직접 확인하십시오OS 앱은 다른 버전의 앱과 동일한 경험을 제공하지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/clarify-description-before_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/clarify-description-before_2x.png)

A description that might lead people to expect access to 90,000 maps on their Apple Watch
> Apple Watch에서 90,000개의 지도에 대한 액세스를 기대할 수 있는 설명
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/clarify-description-after_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/clarify-description-after_2x.png)

A description that clarifies how the subscription works on Apple Watch in contrast with other devices
> 다른 장치와 비교하여 Apple Watch에서 구독이 작동하는 방식을 설명하는 설명
>




**Consider using a modal sheet to display the required information.** After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single, focused view. Even though people must scroll the view to access all the information, displaying it in a modal sheet helps your app UI remain streamlined and concise. Also, a modal sheet’s default Close button makes it easy for people to return to your free content with one tap. If you create a custom sign-up view instead of using a modal sheet, design a focused experience that includes a Close or Cancel button that lets people return to your free content.
> 필요한 정보를 표시하기 위해 모달 시트를 사용하는 것을 고려해 보십시오. 구독 제안에 대해 자세히 알아보기 위해 사람들이 사용자의 요청에 응답한 후 모달 시트를 사용하여 모든 필수 항목을 하나의 초점 뷰로 표시할 수 있습니다. 모든 정보에 액세스하려면 보기를 스크롤해야 하지만 모달 시트로 표시하면 앱 UI가 간소화되고 간결하게 유지됩니다. 또한 모달 시트의 기본 닫기 버튼을 사용하면 한 번의 탭으로 자유로운 콘텐츠로 쉽게 돌아갈 수 있습니다. 모달 시트를 사용하는 대신 사용자 정의 등록 보기를 만드는 경우, 사용자가 무료 콘텐츠로 돌아갈 수 있는 닫기 또는 취소 단추를 포함하는 집중적인 환경을 설계하십시오.
>




**Make subscription options easy to compare on a small screen.** People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you might present subscription options in your watchOS app:
> 작은 화면에서 쉽게 비교할 수 있는 구독 옵션을 만듭니다. 사람들은 각 구독 옵션을 선택하기 전에 각 구독 옵션의 조건을 이해해야 합니다. 각 옵션의 기간 및 할인 정보를 검색하고 비교하기 쉬운 간결한 방식으로 표시하는 것을 목표로 합니다. 다음은 시계에서 구독 옵션을 표시할 수 있는 두 가지 방법입니다OS 앱:
>




- Display each option in a separate button. Using one button per payment option lets people start the signup process with one tap. In this design, it’s important to lock up each button with its description so that people can see how these elements are related, especially while scrolling.
- >  각 옵션을 별도의 단추에 표시합니다. 결제 옵션당 버튼 하나를 사용하면 한 번의 탭으로 가입 절차를 시작할 수 있습니다. 이 설계에서는 특히 스크롤하는 동안 이러한 요소들이 어떻게 관련되어 있는지 사람들이 볼 수 있도록 각 단추를 설명과 함께 잠그는 것이 중요합니다.

- Display a list of options, followed by a button people tap to start the signup process. Using a list to display one option per row gives you a compact design that minimizes scrolling while making subscription choices easy to scan and understand. In this design, the button’s title can update to reflect the chosen option.
- >  옵션 목록을 표시한 다음 사용자가 버튼을 눌러 등록 프로세스를 시작합니다. 목록을 사용하여 행당 하나의 옵션을 표시하면 스크롤을 최소화하는 동시에 헤드라인 등록 선택사항을 쉽게 검색하고 이해할 수 있는 소형 설계가 가능합니다. 이 설계에서는 선택한 옵션을 반영하도록 버튼 제목을 업데이트할 수 있습니다.


![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/lock-up-option-information_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/lock-up-option-information_2x.png)

One payment option per button

![https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/list-option-information_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/images/list-option-information_2x.png)

One payment option per list row, followed by a button that updates to display the chosen option
> 목록 행당 하나의 결제 옵션을 선택한 후 선택한 옵션을 표시하도록 업데이트하는 단추
>



