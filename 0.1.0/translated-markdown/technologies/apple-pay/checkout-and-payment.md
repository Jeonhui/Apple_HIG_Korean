# **[technologies-apple-pay] checkout-and-payment**

People appreciate using Apple Pay to make purchases quickly and easily. You can enhance the purchase experience in your app or website by creating a streamlined checkout process and presenting a customized payment sheet that lets people promptly authorize payment and complete their transaction.
> 사람들은 빠르고 쉽게 구매하기 위해 애플페이를 사용하는 것을 좋아한다. 간소화된 체크아웃 프로세스를 만들고 사람들이 신속하게 결제를 승인하고 거래를 완료할 수 있는 맞춤형 결제 시트를 제시하여 앱 또는 웹 사이트에서 구매 경험을 향상시킬 수 있습니다.
>




# **Streamline the checkout process**

**Provide a cohesive checkout experience.** It’s best when the entire checkout flow feels tightly integrated with your app or website. To strengthen people’s perception of integration, use your branding throughout the checkout experience and avoid opening different pages or windows. For website checkout flows in particular, opening new windows during the process can cause confusion and may even lead people to think they’ve been handed off to a different website.
> 통합된 체크아웃 환경을 제공하십시오. 전체 체크아웃 흐름이 당신의 앱이나 웹사이트와 긴밀하게 통합되어 있을 때가 가장 좋습니다. 통합에 대한 사람들의 인식을 강화하기 위해 체크아웃 환경에서 브랜드를 사용하고 다른 페이지나 창을 열지 마십시오. 특히 웹 사이트 체크아웃 흐름의 경우 프로세스 중에 새 창을 여는 것은 혼란을 야기할 수 있으며 심지어 사람들이 다른 웹 사이트로 전달되었다고 생각하게 할 수도 있습니다.
>




**If Apple Pay is enabled, assume the person wants to use it.** Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.
> Apple Pay가 활성화된 경우 사용자가 Apple Pay 버튼을 첫 번째 결제 옵션으로 제시하거나 다른 옵션보다 크게 표시하거나 선을 사용하여 다른 옵션과 시각적으로 구분하는 것을 고려해 보십시오.
>




**Accelerate single-item purchases with Apple Pay buttons on product detail pages.** In addition to offering a shopping cart, consider putting Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated in this way should be for an individual item only, and should exclude any items that already reside in the shopping cart. If the shopping cart contains an item purchased directly from a product detail page, remove the item from the cart after the purchase is complete.
> 제품 상세페이지의 애플페이 버튼으로 단품 구매를 가속화한다. 쇼핑카트를 제공하는 것 외에도, 사람들이 개별 상품을 빠르게 구매할 수 있도록 제품 상세페이지에 애플페이 버튼을 넣는 것을 고려한다. 이러한 방식으로 시작되는 구매는 개별 품목에 대해서만 수행해야 하며 쇼핑 카트에 이미 있는 모든 품목은 제외해야 합니다. 장바구니에 제품 세부 정보 페이지에서 직접 구매한 항목이 포함되어 있는 경우, 구매가 완료된 후 카트에서 해당 항목을 제거하십시오.
>




**Accelerate multi-item purchases with express checkout.** Consider providing an express checkout feature that immediately displays the payment sheet, allowing people to purchase multiple items quickly using a single shipping method and destination. If you offer a coupon or promotional code, you can enhance the express checkout experience by letting people enter it on the payment sheet.
> 익스프레스 체크아웃으로 멀티 아이템 구매를 가속화합니다. 결제 시트를 즉시 표시할 수 있는 익스프레스 체크아웃 기능을 제공하여 단일 배송 방법과 목적지를 사용하여 여러 아이템을 빠르게 구매할 수 있도록 하는 것을 고려해 보십시오. 쿠폰이나 프로모션 코드를 제공하면 결제 시트에 입력할 수 있어 익스프레스 체크아웃 경험을 높일 수 있다.
>




**Collect necessary information, like color and size options, before people reach the Apple Pay button.** When additional information is needed at checkout time — perhaps because the customer forgot to choose an option — gracefully point out the problem and help them correct it. Use highlighting or warning text to identify missing information, and automatically navigate to the problematic field so people can correct it quickly and complete their purchase.
> 사용자가 Apple Pay 버튼을 클릭하기 전에 색상 및 크기 옵션과 같은 필요한 정보를 수집합니다. 체크아웃 시간에 추가 정보가 필요할 때(고객이 옵션을 선택하는 것을 잊었기 때문일 수도 있음) 문제를 올바르게 지적하고 해결하는 데 도움을 줍니다. 강조 표시 또는 경고 텍스트를 사용하여 누락된 정보를 식별하고 문제가 있는 필드로 자동 이동하여 사람들이 빠르게 수정하고 구매를 완료할 수 있습니다.
>




**Collect optional information before checkout begins.** There’s no way to input optional data — like gift messages or delivery instructions — on the payment sheet, so collect this information ahead of time or even after the purchase is complete.
> 결제 시트에 선물 메시지나 배송 지침과 같은 선택적 데이터를 입력할 수 없으므로 미리 또는 구매가 완료된 후에도 이 정보를 수집할 수 있습니다.
>




**Gather multiple shipping methods and destinations before showing the payment sheet.** The payment sheet lets people select a single shipping method and destination for an entire order. If your customers can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay checkout begins, instead of on the payment sheet.
> 결제 시트를 보여주기 전에 여러 배송 방법과 배송지를 수집하십시오. 결제 시트를 사용하면 전체 주문에 대해 단일 배송 방법과 배송지를 선택할 수 있습니다. 고객이 주문에 따라 개별 품목에 대해 다른 배송 방법과 도착지를 선택할 수 있는 경우, 결제 시트 대신 Apple Pay 체크아웃이 시작되기 전에 해당 세부 정보를 수집하십시오.
>




**For in-store pickup, help people choose a pickup location before displaying the payment sheet.** After a customer chooses the pickup location they want, use the read-only format to display the location’s address on the payment sheet. For developer guidance, see [Displaying a read-only pickup address](https://developer.apple.com/documentation/passkit/pkpaymentrequest/displaying_a_read-only_pickup_address).
> 매장 내 픽업의 경우 결제 시트를 표시하기 전에 사람들이 픽업 위치를 선택할 수 있도록 도와줍니다. 고객이 원하는 픽업 위치를 선택한 후 읽기 전용 형식을 사용하여 결제 시트에 위치의 주소를 표시합니다. 개발자 지침은 읽기 전용 픽업 주소 표시를 참조하십시오.
>




**Prefer information from Apple Pay.** Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout to reduce potential corrections.
> Apple Pay의 정보를 선호합니다. Apple Pay 정보가 완전하고 최신이라고 가정합니다. 앱이나 웹 사이트에 기존 연락처, 배송 및 결제 정보가 있더라도 체크아웃 중에 Apple Pay에서 최신 정보를 가져오는 것을 고려하여 수정 가능성을 줄입니다.
>




**Avoid requiring account creation prior to purchase.** If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate as many registration fields as possible using information provided by the payment sheet during checkout.
> 구매 전에 계정을 생성하도록 요구하지 마십시오. 사람들이 계정을 등록하려면 주문 확인 페이지에서 그렇게 하도록 요청하십시오. 체크아웃 시 결제 시트에서 제공하는 정보를 사용하여 가능한 한 많은 등록 필드를 미리 입력합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/paymentSheet-before-account_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/paymentSheet-before-account_2x.png)

**Report the result of the transaction so that people can view it in the payment sheet.** In failure cases, the payment sheet can display the errors that you provide, so people can take steps to fix the problem.
> 거래 결과를 사람들이 지불 시트에서 볼 수 있도록 보고하고, 실패한 경우 지불 시트는 사용자가 제공한 오류를 표시할 수 있으므로 문제를 해결하기 위한 조치를 취할 수 있습니다.
>




**Display an order confirmation or thank-you page.** After the payment sheet shows the result of the transaction, display an order confirmation page to thank people for their purchase, provide details about when the order will ship, and indicate how to check its status. Listing Apple Pay on the confirmation page isn’t necessary, but if you do, show it after the last four digits of the account used to process the transaction or as a separate note. For example: ”1234 (Apple Pay)” or ”Paid with Apple Pay.”
> 주문확인서 또는 감사페이지를 표시하며, 결제시트에 거래결과가 표시된 후 주문확인페이지를 표시하여 구매자에게 구매에 대한 감사를 표시하고, 주문이 언제 발송되는지 상세정보를 제공하며, 주문상태를 확인할 수 있습니다. 확인 페이지에 Apple Pay를 나열할 필요는 없지만, 나열할 경우 거래를 처리하는 데 사용된 계정의 마지막 네 자리 뒤에 표시하거나 별도의 메모로 표시하십시오. 예를 들어 "1234(Apple Pay)" 또는 "Apple Pay로 결제"입니다
>




# **Customize the payment sheet**

**Only present and request essential information.** People may get confused or have privacy concerns if the payment sheet includes extraneous information. For example, it makes sense to see a contact email address but not a shipping address if the purchase is a gift card that will be delivered electronically. Showing or asking for a shipping address in this scenario may give the false impression that something will be physically delivered.
> 필수 정보만 제시하고 요청하십시오. 지불 시트에 관련 없는 정보가 포함되어 있으면 사람들이 혼란을 겪거나 개인 정보에 대한 우려가 있을 수 있습니다. 예를 들어, 구매가 전자적으로 배달되는 기프트 카드인 경우 배송 주소가 아닌 연락처 전자 메일 주소를 보는 것이 의미가 있습니다. 이 시나리오에서 배송 주소를 표시하거나 요청하면 무언가가 물리적으로 배달될 것이라는 잘못된 인상을 줄 수 있습니다.
>




**Display the active coupon or promotional code, or give people a way to enter it.** For example, if people can enter a code before the payment sheet appears, displaying it on the sheet can reassure them that the code works as they expect. Alternatively, enabling code entry on the payment sheet can be particularly beneficial in an express checkout flow.
> 사용 중인 쿠폰이나 프로모션 코드를 표시하거나 사용자에게 입력할 수 있는 방법을 제공합니다. 예를 들어, 지불 시트가 나타나기 전에 코드를 입력할 수 있는 경우 이를 시트에 표시하면 코드가 예상대로 작동한다는 것을 확신할 수 있습니다. 대안적으로, 지불 시트에서 코드 입력을 가능하게 하는 것은 익스프레스 체크아웃 흐름에서 특히 유익할 수 있다.
>




**Let people choose the shipping method in the payment sheet.** To the extent space permits, show a clear description, a cost, and, optionally, an estimated delivery or pickup date — or range of dates — for each available option. In iOS 15 and later, you can take advantage of the shipping method’s calendar and time-zone support to provide accurate delivery or pickup information, regardless of the customer’s current location. For developer guidance, see [PKDateComponentsRange](https://developer.apple.com/documentation/passkit/pkdatecomponentsrange).
> 사람들이 지불 시트에서 배송 방법을 선택할 수 있도록 합니다. 공간이 허용하는 범위 내에서 각 사용 가능한 옵션에 대해 명확한 설명, 비용, 그리고 선택적으로 예상 배송 또는 픽업 날짜 또는 날짜 범위를 표시합니다. iOS 15 이상에서는 배송 방법의 캘린더 및 시간대 지원을 활용하여 고객의 현재 위치에 상관없이 정확한 배송 또는 픽업 정보를 제공할 수 있습니다. 개발자 지침은 PKDate 구성 요소 범위를 참조하십시오.
>




**For in-store pickup, consider letting people choose a pickup window that works for them.**You can use the shipping method to supply a range of dates and times from which people can choose.
> 매장 내 픽업의 경우 사용자가 자신에게 적합한 픽업 창을 선택하도록 허용하는 것이 좋습니다.발송 방법을 사용하여 사용자가 선택할 수 있는 날짜 및 시간 범위를 제공할 수 있습니다.
>




**Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring, and future payments.** A line item includes a label and cost; a line item for a recurring payment can also include a frequency. Don’t use line items to show an itemized list of products that make up the purchase. For developer guidance, see [paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems); for guidance on donations, see [Donations](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations/#donations).
> 라인 항목을 사용하여 추가 요금, 할인, 보류 중인 비용, 추가 기부, 반복 및 향후 지불에 대해 설명합니다. 라인 항목에는 레이블과 비용이 포함되며, 반복 지불에 대한 라인 항목에는 빈도도 포함될 수 있습니다. 구매를 구성하는 제품의 항목별 목록을 표시하기 위해 라인 항목을 사용하지 마십시오. 개발자 지침은 지불 요약을 참조하십시오항목: 기부에 대한 지침은 기부를 참조하십시오.
>




• [iOS](../technologies/apple-pay/checkout-and-payment#)
• [Web](../technologies/apple-pay/checkout-and-payment#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-additionalcharges-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-additionalcharges-2_2x.png)


**Keep line items short.** Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.
> 줄 항목을 짧게 유지합니다. 줄 항목을 특정하고 쉽게 한 눈에 알 수 있도록 합니다. 가능할 때마다 선 항목을 한 줄에 맞춥니다.
>




**Provide a business name after the word *Pay* on the same line as the total.** Use the same business name people will see when they look for the charge on their bank or credit card statement. This provides reassurance that payment is going to the right place. For example: Pay [Business_Name].
> 총계와 같은 줄에 Pay라는 단어 뒤에 사업명을 입력하세요. 사람들이 은행이나 신용카드 명세서에서 요금을 찾을 때 볼 수 있는 것과 같은 사업명을 사용하세요. 이것은 지불이 올바른 곳으로 가고 있다는 확신을 준다. 예: [Business_Name]을 지불합니다.
>




**If you’re not the end merchant, specify both your business name and the end merchant’s name in the payment sheet.** There are a few ways your app, App Clip, or website might help people make a purchase from an end merchant that’s unrelated to your company. For example, a marketplace app can help people make a purchase from an end merchant they might not recognize. Another example is an app that offers a self-checkout service people can use to pay for an item in an end merchant’s physical store without visiting the store’s checkout counter. In scenarios like these, people might not realize two businesses are involved in the transaction, so it’s essential to name both businesses and clarify their roles. When your app acts as an intermediary for an end merchant, clearly and succinctly describe the situation in the Pay line of the payment sheet, using something like Pay [End_Merchant_Business_Name (via Your_Business_Name)].
> 최종 판매자가 아닌 경우 결제 시트에 사업자 이름과 최종 판매자 이름을 모두 지정하십시오. 앱, 앱 클립 또는 웹 사이트를 사용하여 회사와 무관한 최종 판매자로부터 구매하는 데 도움이 되는 몇 가지 방법이 있습니다. 예를 들어, 마켓플레이스 앱은 사람들이 인식하지 못할 수도 있는 최종 판매자로부터 구매하는 것을 도울 수 있다. 또 다른 예는 사람들이 매장의 계산대를 방문하지 않고 최종 판매자의 물리적 매장에서 물건을 지불할 때 사용할 수 있는 셀프 계산 서비스를 제공하는 앱이다. 이러한 시나리오에서 사람들은 두 개의 사업체가 거래에 관련되어 있다는 것을 깨닫지 못할 수 있으므로, 두 사업체의 이름을 지정하고 그들의 역할을 명확히 하는 것이 필수적이다. 앱이 최종 판매자의 중개자 역할을 할 때는 Pay [End_Merchant_Business_Name (Your_Business_Name을 통해)]과 같은 방법을 사용하여 지불 시트의 Pay 라인에 상황을 명확하고 간결하게 설명하십시오.
>




**Clearly disclose when additional costs may be incurred after payment authorization.** In some cases, the total cost may be unknown at checkout time. For example, the price of a car ride based on distance or time might change after checkout. Or, a customer might want to add a tip after a product has been delivered. In situations like these, and when local regulations allow, you can provide a clear explanation in the payment sheet and a subtotal marked as ”Amount Pending.” If you are preauthorizing a specific amount, be sure the payment sheet accurately reflects this information.
> 결제승인후 추가비용 발생시기를 명확히 밝히며, 체크아웃시 총비용을 알 수 없는 경우도 있습니다. 예를 들어, 거리나 시간에 따른 차량 승차 가격은 체크아웃 후에 변경될 수 있습니다. 또는 고객이 제품이 배송된 후 팁을 추가하려고 할 수도 있습니다. 이러한 상황에서, 그리고 지역 규정이 허용할 때, 당신은 지불 시트에 명확한 설명과 "미결 금액"으로 표시된 소계를 제공할 수 있다 특정 금액을 사전 승인하는 경우 지불 시트에 이 정보가 정확하게 반영되어 있는지 확인하십시오.
>




**Handle data entry and payment errors gracefully.** If an error occurs during checkout, help people resolve it quickly so they can complete their transaction. For related guidance, see [Data validation](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/handling-errors/#data-validation).
> 데이터 입력 및 결제 오류를 정상적으로 처리하고, 체크아웃 중 오류가 발생할 경우 신속하게 해결하여 거래를 완료할 수 있도록 도와줍니다. 관련 지침은 데이터 유효성 검사를 참조하십시오.
>




### **Displaying a website icon**

Many websites provide an icon that can be displayed with bookmarks, in URL fields, or on a device’s Home screen. Websites that support Apple Pay can display this icon in a summary view and in the payment sheet of the connected device that’s used to authorize payment. The icon provides visual reassurance that payment is going to the right place.
> 많은 웹 사이트에서 책갈피, URL 필드 또는 장치의 홈 화면에 표시할 수 있는 아이콘을 제공합니다. Apple Pay를 지원하는 웹 사이트는 이 아이콘을 요약 보기 및 결제를 승인하는 데 사용되는 연결된 장치의 결제 시트에 표시할 수 있습니다. 이 아이콘은 결제가 올바른 위치로 진행되고 있다는 시각적인 확신을 제공합니다.
>




If your website supports Apple Pay, provide an icon in the following sizes for use in the summary view and the payment sheet:
> 웹 사이트에서 Apple Pay를 지원하는 경우 요약 보기 및 결제 시트에 사용할 수 있도록 다음 크기의 아이콘을 제공하십시오:
>




| @2x | @3x |
| --- | --- |
| 60x60 pt (120x120 px @2x) | 60x60 pt (180px180 px @3x) |

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webicon-payment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webicon-payment_2x.png)
