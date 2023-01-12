# **[technologies-apple-pay] subscriptions-and-donations**

If you offer subscriptions or support other types of recurring payments, or if you’re a non-profit that accepts donations, follow these guidelines.
> 구독을 제공하거나 다른 유형의 반복 지불을 지원하거나 기부를 받는 비영리 단체인 경우 다음 지침을 따르십시오.
>




# **Subscriptions**

Your app or website can use Apple Pay to request authorization for recurring fees. A recurring fee can be a fixed amount, such as a monthly movie ticket subscription, or — when local regulations allow — a variable amount like a weekly grocery order. The initial authorization can also include discounts and additional fees.
> 앱 또는 웹 사이트는 Apple Pay를 사용하여 반복 수수료에 대한 승인을 요청할 수 있습니다. 정기 요금은 월별 영화 티켓 구독과 같은 고정 금액이거나, 지역 규정에 따라 매주 식료품 주문과 같은 변동 금액일 수 있습니다. 초기 승인에는 할인 및 추가 수수료도 포함될 수 있습니다.
>




---

### • [iOS](../technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-fixedsubscription_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-fixedsubscription_2x.png)

Fixed subscription

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-variablesubscription_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-variablesubscription_2x.png)

Variable subscription (where local regulations allow)
> 가변 구독(지역 규정이 허용하는 경우)
>




### • [Web](../technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-fixed_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-fixed_2x.png)

Fixed subscription

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-variable_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-variable_2x.png)

Variable subscription (where local regulations allow)
> 가변 구독(지역 규정이 허용하는 경우)
>




---

**Clarify subscription details before showing the payment sheet.** Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can reiterate the billing frequency on the payment sheet.
> 지불 시트를 보여주기 전에 구독 세부 사항을 명확히 하십시오. 반복 지불을 승인하도록 요청하기 전에, 청구 빈도 및 기타 서비스 약관을 완전히 이해했는지 확인하십시오. 결제 시트에서 청구 빈도를 반복할 수 있습니다.
>




**Include line items that reiterate billing frequency, discounts, and additional upfront fees.**Use these line items to remind people what they’re authorizing. If no payment is required at authorization time, clearly disclose when billing will occur.
> 청구 빈도, 할인 및 추가 선불 수수료를 반복하는 라인 항목을 포함합니다.다음 줄 항목을 사용하여 사용자가 권한을 부여한 내용을 알려줍니다. 승인 시점에 지불이 필요하지 않은 경우 청구가 발생할 시기를 명확히 공개합니다.
>




---

### • [iOS](../technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-no-payment-required_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-no-payment-required_2x.png)

No payment required at authorization

### • [Web](../technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay-Web-ZeroPayment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay-Web-ZeroPayment_2x.png)

No payment required at authorization

---

**Clarify the current payment amount in the total line.** Make sure people know the amount they’re being billed at the time of authorization.
> 현재 결제 금액을 총계에 명시하고 승인 시 청구되는 금액을 사람들이 알 수 있도록 합니다.
>




**Only show the payment sheet when a subscription change results in additional fees.** When the someone changes a subscription, authorization isn’t necessary if the cost decreases or remains the same.
> 구독 변경으로 인해 추가 요금이 발생할 때만 지불 시트를 표시하고, 구독을 변경할 때 비용이 줄거나 그대로 유지되면 승인이 필요하지 않습니다.
>




# **Donations**

[Approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/) can use Apple Pay to accept donations.
> 승인된 비영리 단체는 Apple Pay를 사용하여 기부금을 받을 수 있습니다.
>




**Use a line item to denote a donation.** Display a line item on the payment sheet that reminds people they’re authorizing a donation; for example, display Donation $50.00.
> 기부를 나타내는 줄 항목을 사용합니다. 지불 시트에 기부를 승인하는 사람들에게 알려주는 줄 항목을 표시합니다. 예를 들어, 기부 $50.00.
>




**Streamline checkout by offering predefined donation amounts.** You can reduce steps in the donation process by offering one-step recommended donations, like $25, $50, $100. Be sure to include an Other Amount option too, so people can customize the donation if they prefer.
> 미리 정의된 기부 금액을 제공하여 계산을 간소화합니다. $25, $50, $100과 같은 한 단계 권장 기부를 제공하여 기부 과정의 단계를 줄일 수 있습니다. 사람들이 원할 경우 기부를 사용자 지정할 수 있도록 기타 금액 옵션도 포함해야 합니다.
>



