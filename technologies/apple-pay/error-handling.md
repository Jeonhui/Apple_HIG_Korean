# **[technologies-apple-pay] error-handling**

Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve problems quickly and complete their transaction.
> 체크아웃 또는 결제 처리 중 문제가 발생할 때 명확하고 실행 가능한 지침을 제공하여 사람들이 문제를 신속하게 해결하고 거래를 완료할 수 있도록 합니다.
>




# **Data validation**

Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the transaction. Use these opportunities to check for data entry problems and to provide clear and consistent messaging.
> 앱 또는 웹 사이트는 결제 시트가 나타날 때, 사용자가 결제 시트의 특정 필드 값을 변경할 때, 그리고 거래를 인증한 후에 사용자 입력에 응답할 수 있습니다. 이러한 기회를 통해 데이터 입력 문제를 확인하고 명확하고 일관된 메시징을 제공할 수 있습니다.
>




### • [iOS](../technologies/apple-pay/handling-errors#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error_2x.png)

Payment sheet error messaging

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error2_2x.png)

Custom detail view error messaging

### • [Web](../technologies/apple-pay/handling-errors#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorA_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorA_2x.png)

Payment sheet error messaging

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorB_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorB_2x.png)

Custom detail view error messaging


When data is invalid, system-provided error messaging calls attention to relevant fields on the payment sheet. People can choose a field to view additional details and resolve the problem. Provide customized error messages for the detail view that appears when people choose a problematic field.
> 데이터가 잘못된 경우 시스템에서 제공하는 오류 메시지는 지급 시트의 관련 필드에 주의를 환기시킵니다. 사용자는 필드를 선택하여 추가 세부 정보를 보고 문제를 해결할 수 있습니다. 사용자가 문제가 있는 필드를 선택할 때 나타나는 세부 정보 보기에 대해 사용자 정의된 오류 메시지를 제공합니다.
>




For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS, watchOS) and [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web) (web).
> 개발자 지침은 PK 지불을 참조하십시오권한 부여 보기컨트롤러 위임(iOS, watch)웹(웹)에서 Apple Pay와 OS)를 사용할 수 있습니다.
>




**NOTE**For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction. Prior to authorization, only the card type and a redacted shipping address are accessible. It’s critical to display errors when authorization fails, but to the extent possible, your app should also attempt to validate available information and report problems before authorization.
> 참고 개인 정보 보호를 위해 사용자의 앱 또는 웹 사이트는 사용자가 트랜잭션을 승인할 때까지 데이터에 대한 액세스가 제한됩니다. 승인 전에는 카드 유형과 수정된 배송 주소만 액세스할 수 있습니다. 권한 부여가 실패할 때 오류를 표시하는 것은 매우 중요하지만, 가능한 한 앱은 권한 부여 전에 사용 가능한 정보를 확인하고 문제를 보고해야 합니다.
>




**Avoid forcing compliance with your business logic.** Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction. Let people enter phone numbers in multiple formats — such as with and without dashes, and with and without a country code — without producing an error.
> 비즈니스 로직을 강제로 준수하지 않도록 하십시오. 관련 없는 데이터를 무시하고 가능한 경우 누락된 데이터를 추론할 수 있을 정도로 지능적인 데이터 검증 프로세스를 설계하십시오. 예를 들어, 앱에 5자리 우편 번호가 필요한데 누군가 Zip+4 코드를 입력한 경우 수정을 요청하기보다는 추가 숫자를 무시하십시오. 사람들이 전화 번호를 대시 포함 및 포함하지 않고, 국가 코드 포함 및 포함되지 않은 여러 형식으로 오류 없이 입력할 수 있습니다.
>




