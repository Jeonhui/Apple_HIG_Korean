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




