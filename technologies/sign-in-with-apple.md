# **[technologies] sign-in-with-apple**

# Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.
> Apple 로그인은 앱과 웹 사이트에 로그인하는 빠르고 사적인 방법을 제공하여 사람들에게 신뢰할 수 있는 일관된 경험을 제공하고 여러 계정과 암호를 기억할 필요가 없는 편리함을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-SIWA-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-SIWA-intro_2x.png)

Supporting Sign in with Apple lets people use the Apple ID they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see [Authentication Services](http://developer.apple.com/documentation/authenticationservices).
> Apple로 로그인을 지원하면 이미 로그인하거나 등록해야 하는 Apple ID를 사용할 수 있으며 양식 작성, 전자 메일 주소 확인 및 암호 선택을 생략할 수 있습니다. 이름과 전자 메일 주소를 묻기로 선택한 경우 사용자는 메시지를 자동으로 개인 전자 메일 주소로 릴레이하는 고유한 임의 전자 메일 주소를 공유할 수 있습니다. 개발자 지침은 인증 서비스를 참조하십시오.
>




You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.
> Apple 이외의 플랫폼을 포함한 모든 플랫폼의 모든 버전 또는 웹 사이트에서 Apple로 로그인을 제공할 수 있습니다.
>




Sign in with Apple makes it easy for people to authenticate with Face ID or Touch ID and has two-factor authentication built in for an added layer of security. Apple does not use Sign in with Apple to profile users or their activity in apps.
> 애플 로그인은 사람들이 페이스ID나 터치ID로 쉽게 인증할 수 있게 해주며, 보안 계층을 강화하기 위해 2단계 인증이 내장되어 있다. Apple은 Apple에서 사용자 또는 사용자의 앱 활동을 프로파일링하는 데 Apple 로그인을 사용하지 않습니다.
>




# **Offering Sign in with Apple**
> Apple로 로그인 제공
>




Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.
> 다음 지침에 따라 사용자가 가장 편리할 때 Apple에 로그인할 수 있습니다.
>




**Ask people to sign in only in exchange for value.** People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.
> 사람들에게 가치를 대가로 로그인하도록 요청하십시오. 사람들은 사용자가 로그인을 요청하는 이유를 이해해야 로그인 혜택에 대한 간략하고 접근 가능한 설명을 표시할 수 있습니다. 예를 들어, 로그인을 통해 앱 경험을 개인화하거나, 추가 기능에 액세스하거나, 데이터를 동기화할 수 있다고 사람들에게 말하고 싶을 수 있습니다.
>




**Delay sign-in as long as possible.** People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.
> 사람들은 유용한 일을 하기 전에 강제로 로그인해야 할 때 앱을 버리는 경우가 많습니다. 약속을 하기 전에 그들에게 당신의 앱에 익숙해질 기회를 주세요. 예를 들어, 라이브 스트리밍 앱은 사람들이 무언가를 스트리밍하기 위해 로그인하기 전에 이용 가능한 콘텐츠를 탐색하도록 할 수 있다.
>




**If you require an account, ask people to set it up before offering any sign-in options.** Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.
> 계정이 필요한 경우 로그인 옵션을 제공하기 전에 계정을 설정하도록 요청하십시오. 계정이 필요한 이유를 설명하는 것부터 시작하십시오. 그런 다음 사용자가 계정 설정을 완료한 후 Apple 로그인 및 지원하는 다른 로그인 방법을 제공하여 새 계정에 편리하게 로그인할 수 있는 방법을 선택하도록 합니다.
>




**Consider letting people link an existing account to Sign in with Apple.** When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:
> 사용자가 기존 계정을 Apple로 로그인하도록 허용하는 것을 고려해 보십시오. 이러한 유형의 링크를 지원하면 이미 설정한 계정의 정보에 대한 액세스를 유지하면서 Apple로 로그인을 사용할 수 있습니다. 사용자가 기존 계정에 로그인하기 전이나 후에 계정 연결을 제공할 수 있습니다. 예:
>




- If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
- >  사용자가 Apple과 로그인을 통해 이메일 주소를 공유하고 기존 계정의 주소와 일치하는 경우 해당 계정에 로그인을 연결하도록 제안할 수 있습니다.

- If people used an existing username and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.
- >  사용자가 기존 사용자 이름과 암호를 사용하여 로그인한 경우 계정 설정 보기 또는 다른 논리적 위치에 계정 연결 제안을 표시할 수 있습니다.


**In a commerce app, wait until after people make a purchase before asking them to create an account.** If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.
> 커머스 앱에서, 사람들이 계정을 만들도록 요청하기 전에 사람들이 구매를 할 때까지 기다리십시오. 만약 당신이 게스트 체크아웃 시스템을 지원한다면, 사람들에게 거래가 완료된 후에 계정을 만들 수 있는 빠른 방법을 제공하십시오. 예를 들어, Apple Pay를 지원하는 경우 주문 확인 페이지에서 사용자가 계정을 만들 수 있습니다. Apple Pay 거래 중에 사용자가 이미 이름과 전자 메일 주소를 제공한 경우에는 이 정보를 요청할 필요가 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/create-account-after-purchase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/create-account-after-purchase_2x.png)

**As soon as Sign in with Apple completes, welcome people to their new account.** Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.
> Apple 로그인이 완료되는 대로 새 계정으로 오신 것을 환영합니다. 새 계정을 바로 사용할 수 있도록 도와주십시오. 불필요한 정보를 요청하여 경험을 지연시키지 마십시오.
>




**Indicate when people are currently signed in.** You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.
> 사용자가 현재 로그인한 시간을 나타냅니다. 설정 또는 계정 인터페이스와 같은 위치에 "Apple에서 로그인 사용"과 같은 문구를 표시하여 사용자가 로그인 방법을 확인하도록 도와줄 수 있습니다.
>




# **Collecting data**

People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.
> 사람들은 애플사의 사생활과 편리함에 대해 애플사에 로그인하는 것을 높이 평가한다. 일부 앱이나 웹 사이트에는 생년월일이나 거주 지역과 같은 추가 정보가 필요할 수 있지만, 사람들이 계정을 설정할 때 데이터에 대한 요청을 최소화하는 것이 중요합니다. 추가 데이터가 필요한 이유를 설명하고 수신한 데이터를 명확하게 표시하여 Apple에 로그인하는 사용자의 신뢰를 기반으로 합니다.
>




**Clarify whether the additional data you request is required or just recommended.** If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.
> 요청하는 추가 데이터가 필요한지 아니면 단지 권장되는 것인지를 명확히 합니다. 서비스 조건, 국가 또는 거주 지역, 생년월일 또는 지역의 실제 신분법에 의해 요구되는 정보와 같이 법적 또는 계약적으로 데이터가 필요한 경우 사람들은 다음 사이트에서 추가 정보를 제공해야 한다는 것을 이해해야 합니다계정 설정을 완료해야 합니다. 추가 데이터가 필요하지 않지만 사용자 환경을 개선할 수 있는 경우, 사용자가 요청이 선택 사항임을 알고 정보 제공의 이점을 이해할 수 있도록 도와주십시오.
>




**Don’t ask people to supply a password.** A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.
> 사람들에게 비밀번호를 제공하라고 요구하지 마세요. 애플 로그인의 주요 이점은 사람들이 추가적인 비밀번호를 만들고 기억할 필요가 없다는 것입니다. 앱이나 웹 사이트에서 Apple 로그인 사용을 중지한 사람이 아니라면 암호를 묻지 마십시오.
>




**Avoid asking for a personal email address when people supply a private relay address.** Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:
> 사람들이 개인 릴레이 주소를 제공할 때 개인 전자 메일 주소를 묻는 것을 피하십시오. Apple에서 로그인을 사용하면 확인된 개인 전자 메일 계정으로 메시지를 자동으로 전달하는 개인 릴레이 주소를 공유하도록 선택할 수 있습니다. 이 선택을 존중하고 개인 이메일 주소를 요청하여 이를 무시하지 않는 것이 중요합니다. 이메일 주소를 통해 식별을 요청하는 고객 서비스, 소매 또는 기타 경험을 제시하는 경우 다음을 수행할 수 있습니다:
>




- Make sure that people can view their private relay address in your app or website
- >  사용자가 앱 또는 웹 사이트에서 개인 릴레이 주소를 볼 수 있는지 확인합니다

- Direct people to Settings > Apple ID > Password & Security > Apps using Apple ID to retrieve their private relay address
- >  설정 > Apple ID > 비밀번호 및 보안 > Apple ID를 사용하여 개인 릴레이 주소를 검색하는 앱으로 이동합니다

- Use other identifying values, like an order number or phone number collected as part of a purchase
- >  구매의 일부로 수집된 주문 번호 또는 전화 번호와 같은 다른 식별 값 사용


**Give people a chance to engage with your app before asking for optional data.** As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.
> 선택적 데이터를 요청하기 전에 사용자의 앱에 참여할 수 있는 기회를 제공합니다. 사용자가 사용자의 앱을 사용할 때 사용자와 더 많은 정보를 공유하여 이익을 얻을 수 있는 장소를 찾을 수 있도록 도와줄 수 있습니다. 예를 들어 실시간 텍스트 업데이트를 원하는 경우 연락처 전화 번호를 제공하거나 친구와 게임을 하려는 경우 소셜 네트워크 정보를 제공할 것을 제안할 수 있습니다. 사용자가 선택적 정보를 제공하지 않기로 선택한 경우 사용자가 자신의 계정에 액세스하거나 앱의 모든 기능을 사용하는 것을 막지 마십시오.
>




**Be transparent about the data you collect.** People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a relay address, shows people where to find it in the future. If you don’t display all the data that people provide, they are likely to wonder why you asked for it.
> 수집하는 데이터에 대해 투명해야 합니다. 사람들은 자신과 공유하는 데이터를 어떻게 사용하는지 아는 것을 중요하게 생각합니다. 투명해질 수 있는 한 가지 방법은 사람들이 공유한 이름이나 이메일 주소를 사용하여 사람들을 환영하는 것입니다. 이렇게 하면 이 정보를 사용하는 방법을 설정하는 데 도움이 되며, 릴레이 주소의 경우 나중에 사용자가 정보를 찾을 수 있는 위치를 보여줍니다. 만약 당신이 사람들이 제공하는 모든 데이터를 표시하지 않는다면, 그들은 당신이 왜 그것을 요구했는지 궁금해 할 것이다.
>




# **Displaying buttons**

Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in. If necessary, you can create a custom button to offer Sign in with Apple; for guidelines, see [Creating a custom Sign in with Apple button](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple#creating-a-custom-sign-in-with-apple-button).
> Apple은 사용자가 계정을 설정하고 로그인하는 데 사용할 수 있는 Apple 단추와 함께 로그인을 제공합니다. 필요한 경우 사용자 지정 단추를 만들어 Apple 로그인을 제공할 수 있습니다.
>




**Prominently display a Sign in with Apple button.** Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.
> Apple로 로그인 단추를 눈에 띄게 표시합니다. 다른 로그인 단추보다 작지 않은 Apple로 로그인 단추를 사용하여 다른 사용자가 해당 단추를 스크롤하지 않도록 합니다.
>




# **Using the system-provided buttons**

When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.
> 시스템에서 제공하는 API를 사용하여 Apple로 로그인 버튼을 만들면 다음과 같은 이점이 있습니다.
>




- A button that’s guaranteed to use an Apple-approved appearance
- >  Apple에서 승인한 모양을 사용할 수 있는 버튼

- Assurance that the button’s contents maintain ideal proportions as you change its style
- >  스타일을 변경해도 버튼 내용이 이상적인 비율을 유지하도록 보장

- Automatic translation of the button’s title into the language specified by the device
- >  단추 제목을 장치에서 지정한 언어로 자동 변환

- Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)
- >  UI(iOS, macOS 및 웹) 스타일에 맞게 버튼의 모서리 반지름 구성 지원

- A system-provided alternative text label that lets VoiceOver describe the button
- >  VoiceOver가 버튼을 설명할 수 있도록 시스템에서 제공하는 대체 텍스트 레이블


For developer guidance, see [ASAuthorizationAppleIDButton](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton) (iOS, macOS, and tvOS), [WKInterfaceAuthorizationAppleIDButton](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton) (watchOS), and [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web). You can also visit [Sign in with Apple button](https://appleid.apple.com/signinwithapple/button) to view and adjust live previews of web-based buttons and get the code.
> 개발자 지침은 인증 Apple을 참조하십시오IDButton(iOS, macOS 및 tvOS), WK 인터페이스권한 부여 애플웹에서 ID 버튼(watch OS) 및 Apple 버튼으로 로그인 표시. 또한 Apple 단추로 로그인을 방문하여 웹 기반 단추의 라이브 미리 보기를 보고 조정하고 코드를 가져올 수 있습니다.
>




The system provides several variants of the button title. Depending on the platform on which your content runs, choose the variant that fits the terminology of your sign-in experience and use it consistently throughout your interfaces.
> 이 시스템은 버튼 제목의 몇 가지 변형을 제공합니다. 콘텐츠가 실행되는 플랫폼에 따라 로그인 환경의 용어에 맞는 변형을 선택하고 인터페이스 전체에서 일관되게 사용하십시오.
>




The following button titles are available for iOS, macOS, tvOS, and the web:
> iOS, macOS, tvOS 및 웹에서 사용할 수 있는 단추 제목은 다음과 같습니다:
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-sign-in-with_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-sign-in-with_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-sign-up-with_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-sign-up-with_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-continue-with_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-continue-with_2x.png)

For watchOS, the system provides one title:  Sign in.
> watchOS의 경우, 시스템은 하나의 제목을 제공합니다: 로그인.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-watch-44mm-no-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-watch-44mm-no-background_2x.png)

Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black. Choose the appearance that works best with the background on which the button displays.
> 플랫폼에 따라 시스템은 Apple로 로그인 버튼을 표시하기 위한 최대 세 가지 옵션(흰색, 윤곽선이 있는 흰색, 검은색)을 제공합니다. 단추가 표시되는 배경에 가장 적합한 모양을 선택합니다.
>




### **White**

The white style is available on all platforms and the web. Use this style on dark backgrounds that provide sufficient contrast.
> 흰색 스타일은 모든 플랫폼과 웹에서 사용할 수 있습니다. 어두운 배경에서 충분한 대비를 제공하는 이 스타일을 사용하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-white-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-white-yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-white-no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-white-no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **White with outline**

The white outlined style is available in iOS, macOS, and the web. Use this style on white or light-color backgrounds that don’t provide sufficient contrast with the white button fill. Avoid using this style on a dark or saturated background, because the black outline can add visual clutter; instead, use the [white](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple#white) style to contrast with a dark background.
> 흰색 윤곽의 스타일은 iOS, macOS, 웹에서 사용할 수 있다. 흰색 단추 채우기와 충분한 대비를 제공하지 않는 흰색 또는 밝은 색상 배경에 이 스타일을 사용하십시오. 검은색 윤곽선이 시각적 혼란을 가중시킬 수 있으므로 어둡거나 포화된 배경에서는 이 스타일을 사용하지 마십시오. 대신 흰색 스타일을 사용하여 어두운 배경과 대비하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-outline-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-outline-yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-outline-no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-outline-no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

### **Black**

The black style is available on all platforms and the web. Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds.
> 블랙 스타일은 모든 플랫폼과 웹에서 사용할 수 있다. 이 스타일은 대비가 충분한 흰색 또는 밝은 색상 배경에 사용하고 검은색 또는 어두운 배경에는 사용하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-black-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-black-yes_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-black-no_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-black-no_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black. To contrast with the pure black background of Apple Watch, the watchOS button uses the system-defined dark gray appearance.
> 다른 플랫폼의 검은색 Apple 로그인 단추와 달리 watch OS 단추는 완전히 검은색이 아닌 채우기 색을 사용합니다. 애플 워치의 순수한 검은색 배경과 대조적으로 워치OS 버튼은 시스템 정의 다크 그레이 외관을 사용한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-watch-44mm_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-watch-44mm_2x.png)

### **Button size and corner radius**
> 단추 크기 및 모서리 반지름
>




**Adjust the corner radius to match the appearance of other buttons in your app.** By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a pill-shaped button. For developer guidance, see [cornerRadius](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton/3153030-cornerradius) (iOS and macOS) and [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web).
> 앱의 다른 단추 모양에 맞게 모서리 반지름을 조정합니다. 기본적으로 Apple로 로그인 단추에는 둥근 모서리가 있습니다. iOS, macOS, 웹에서 모서리 반지름을 변경하여 사각 모서리가 있는 버튼이나 알약 모양의 버튼을 만들 수 있습니다. 개발자 지침은 웹에서 Radius(iOS 및 macOS) 코너 및 Apple 버튼으로 로그인 표시를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-minimum-corner-radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-minimum-corner-radii_2x.png)

Minimum corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-default-corner-radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-default-corner-radii_2x.png)

Default corner radius

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-maximum-corner-radii_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/apple-id-maximum-corner-radii_2x.png)

Maximum corner radius

**Maintain the minimum button size and margin around the button in iOS, macOS, and the web.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
> iOS, macOS, 웹에서 버튼 주변의 최소 버튼 크기와 여백을 유지하십시오. 버튼 제목은 로케일에 따라 길이가 달라질 수 있습니다. 지침으로 다음 값을 사용하십시오.
>




| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

# **Creating a custom Sign in with Apple button**
> 사용자 정의 Apple로 로그인 단추 만들기
>




If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web. For example, you may want to align logos across multiple sign-in buttons, use buttons that display only a logo, or adjust the button’s font, bezel, or background appearance to coordinate with your UI.
> 인터페이스에 필요한 경우 iOS, macOS 또는 웹용 Apple 단추를 사용하여 사용자 지정 로그인을 만들 수 있습니다. 예를 들어 여러 로그인 단추에 걸쳐 로고를 정렬하거나, 로고만 표시하는 단추를 사용하거나, 단추의 글꼴, 베젤 또는 배경 모양을 조정하여 UI에 맞게 조정할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/custom-sign-in-screens_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/custom-sign-in-screens_2x.png)

Always make sure that people can instantly identify your custom button as a Sign in with Apple button. If your custom button differs too much from the standard one, people may not feel comfortable using it to set up an account or sign in. App Review evaluates all custom Sign in with Apple buttons.
> 항상 사용자 지정 단추를 Apple 로그인 단추로 즉시 식별할 수 있도록 하십시오. 사용자 지정 단추가 표준 단추와 너무 다를 경우 계정을 설정하거나 로그인하는 데 사용하는 데 불편함을 느낄 수 있습니다. App Review는 Apple 버튼을 사용하여 모든 사용자 지정 로그인을 평가합니다.
>




[Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that display either a logo only or a logo and text. The logo files are available in PNG, SVG, and PDF formats, and the artwork for both types of buttons includes both black and white versions. Here are examples of the black and white logo-only art files, each with a background added for visibility.
> Apple Design Resources는 다운로드 가능한 Apple 로고 아트워크를 제공하여 로고만 표시하거나 로고와 텍스트를 표시하는 Apple 단추를 사용하여 사용자 지정 로그인을 만들 수 있습니다. 로고 파일은 PNG, SVG, PDF 형식으로 제공되며, 두 가지 유형의 버튼에 대한 아트워크에는 흑백 버전이 모두 포함됩니다. 다음은 검은색과 흰색 로고 전용 아트 파일의 예이며, 각각은 가시성을 위해 배경이 추가되어 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/black-logo-only_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/black-logo-only_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/white-logo-only_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/white-logo-only_2x.png)

All downloadable logo files include padding that simplifies positioning the logo in a button. Logo-only logo files include horizontal and vertical padding that ensures the correct proportion of the logo relative to the button. In addition to padding that keeps the logo and button correctly proportioned, logo files for buttons with text also include horizontal padding that provides a minimum margin between the logo and the button’s leading edge and title.
> 다운로드 가능한 모든 로고 파일에는 로고를 버튼에 쉽게 배치할 수 있는 패딩이 포함되어 있습니다. 로고 전용 로고 파일에는 버튼에 대한 로고의 정확한 비율을 보장하는 수평 및 수직 패딩이 포함되어 있습니다. 로고와 단추의 비율을 정확하게 유지하는 패딩 외에도 텍스트가 있는 단추의 로고 파일에는 로고와 단추의 선행 모서리 및 제목 사이에 최소 여백을 제공하는 수평 패딩도 포함되어 있습니다.
>




Use only the logo artwork downloaded from [Apple Design Resources](https://developer.apple.com/design/resources/); never create a custom Apple logo. As you create a custom Sign in with Apple button, follow these guidelines for using the downloadable logo file:
> Apple Design Resources에서 다운로드한 로고 아트워크만 사용하고, 사용자 지정 Apple 로고는 만들지 마십시오. Apple로 사용자 지정 로그인 단추를 만들 때 다운로드 가능한 로고 파일을 사용하기 위한 다음 지침을 따르십시오:
>




- Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
- >  로고 파일을 사용하여 단추에 Apple 로고를 배치합니다. 단추로고를 단추로 사용하지 마십시오.

- Match the height of the logo file to the height of the button.
- >  로고 파일의 높이를 버튼의 높이와 일치시킵니다.

- Don’t crop the logo file.
- >  로고 파일을 자르지 마십시오.

- Don’t add vertical padding.

To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.
> 사용자 지정 단추가 시스템에서 제공하는 Apple 로그인 단추와 시각적으로 일치하는지 확인하려면 다음 특성을 변경하지 마십시오.
>




- Titles. Use only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*.
- >  제목. Apple 로그인, Apple 로그인 또는 Apple 계속만 사용합니다.

- General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.
- >  일반적인 모양. 로고와 텍스트를 결합하는 단추는 항상 직사각형이며, 로고 전용 단추는 원형 또는 직사각형일 수 있습니다.

- Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.
- >  로고 및 제목 색상. 단추 내에서 두 항목은 모두 검은색 또는 흰색이어야 합니다. 사용자 지정 색상을 사용하면 안 됩니다.


To coordinate with your app design, you can change:
> 앱 디자인에 맞춰 다음을 변경할 수 있습니다:
>




- Title font. You can also adjust the font’s weight and size.
- >  제목 글꼴. 글꼴의 무게와 크기를 조정할 수도 있습니다.

- Title case. You can capitalize every letter in the title.
- >  타이틀 케이스. 제목의 모든 문자를 대문자로 쓸 수 있습니다.

- Background appearance. The overall color should remain black or white. If necessary, you can include a subtle texture or gradient to help the button harmonize with your interface.
- >  배경 모양. 전체 색상은 검은색 또는 흰색으로 유지되어야 합니다. 필요한 경우 단추가 인터페이스와 조화를 이루도록 미묘한 질감이나 그라데이션을 포함할 수 있습니다.

- Button corner radius. You can use a corner radius value that matches the other buttons in your UI.
- >  단추 모서리 반지름. UI의 다른 버튼과 일치하는 모서리 반지름 값을 사용할 수 있습니다.

- Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.
- >  버튼 베젤 및 섀도. 예를 들어 스트로크를 사용하여 버튼 베젤을 강조하거나 드롭 섀도우를 추가할 수 있습니다.


### **Custom buttons with a logo and text**
> 로고와 텍스트가 있는 사용자 정의 단추
>




**Choose the format of the logo file based on the height of your button.** Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available in small, medium, and large sizes, so you can match logo sizes in all the sign-up buttons you display.
> 버튼 높이를 기준으로 로고 파일 형식을 선택하십시오. SVG와 PDF는 벡터 기반 형식이기 때문에 이 파일들을 버튼 높이에 상관없이 사용할 수 있습니다. PNG 파일은 iOS에서 기본(권장) 버튼 높이인 44포인트 높이의 버튼에서만 사용하십시오. 로고는 소형, 중형 및 대형 크기로 제공되므로 표시하는 모든 등록 단추에서 로고 크기를 일치시킬 수 있습니다.
>




**Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple.** Regardless of the font you choose, the title and button height of your custom button should use the same proportions that the system uses. Using the system font for example, the title’s font size should be 43% of the button’s height — in other words, the button’s height should be 233% of the title’s font size, rounded to the nearest integer. Here are two examples that show these proportions using different sizes of the system font.
> 제목에 시스템 글꼴(예: Apple로 로그인, Apple로 등록 또는 Apple로 계속)을 사용합니다. 선택한 글꼴에 관계없이 사용자 지정 단추의 제목 및 단추 높이는 시스템에서 사용하는 비율과 동일한 비율을 사용해야 합니다. 예를 들어 시스템 글꼴을 사용하면 제목의 글꼴 크기는 단추 높이의 43%여야 합니다. 즉, 단추 높이는 제목 글꼴 크기의 233%여야 하며 가장 가까운 정수로 반올림됩니다. 다음은 다양한 크기의 시스템 글꼴을 사용하여 이러한 비율을 보여주는 두 가지 예입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/left-aligned-correct-proportions-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/left-aligned-correct-proportions-2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/left-aligned-correct-proportions-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/left-aligned-correct-proportions-1_2x.png)

**In general, preserve the capitalization style of the title.** By default, all variants of the button title capitalize the first word — that is, *Sign* or *Continue* — and *Apple*; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.
> 일반적으로 제목의 대문자 스타일을 유지합니다. 기본적으로 단추 제목의 모든 변형은 첫 번째 단어(즉, 서명 또는 계속)와 Apple을 대문자로 표시합니다. 다른 모든 문자는 소문자입니다. 인터페이스가 대문자만 사용하는 경우가 아니면 이 스타일을 변경하지 마십시오.
>




**Keep the title and logo vertically aligned within the button.** To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title in the button ensures that the title, the logo, and the button stay properly aligned.
> 제목과 로고를 버튼 내에서 수직으로 정렬합니다. 이렇게 하려면 제목을 버튼의 가운데에 수직으로 정렬한 다음 로고 이미지를 추가하여 버튼의 높이와 일치하는지 확인합니다. 로고 이미지에는 상단 및 하단 패딩이 포함되어 있으므로, 버튼에서 제목을 수직으로 정렬하면 제목, 로고 및 버튼이 올바르게 정렬됩니다.
>




**Inset the logo if necessary.** If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.
> 필요한 경우 로고를 삽입하고, Apple 로고를 다른 인증 로고와 수평으로 정렬해야 할 경우 로고와 버튼 앞쪽 가장자리 사이의 공간을 조정할 수 있습니다.
>




**Maintain a minimum margin between the title and the right edge of the button.** The margin should measure at least 8% of the button’s width.
> 제목과 단추의 오른쪽 가장자리 사이에 최소 여백을 유지하십시오. 여백은 단추 너비의 최소 8%를 측정해야 합니다.
>




**Maintain the minimum button size and margin around the button.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
> 단추 주위의 최소 단추 크기와 여백을 유지하십시오. 단추 제목의 길이는 로케일에 따라 달라질 수 있습니다. 지침으로 다음 값을 사용하십시오.
>




| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

### **Custom logo-only buttons**

**Choose the format of the logo file based on the size of your button.** The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.
> 버튼 크기에 따라 로고 파일 형식을 선택하십시오. 로고 전용 버튼의 아트워크는 SVG, PDF, PNG 형식으로 다운로드할 수 있습니다. 모든 크기의 버튼에 벡터 기반 SVG 및 PDF 형식을 사용합니다. 44x44pt를 측정하는 버튼에서만 PNG 형식을 사용합니다.
>




**Don’t add horizontal padding to a logo-only image.** A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.
> 로고 전용 이미지에 가로 패딩을 추가하지 마십시오. 로고 전용 Apple 단추로 로그인하면 항상 가로 세로 비율이 1:1이며, 아트워크에는 이미 모든 면에 올바른 패딩이 포함되어 있습니다.
>




**Use a mask to change the default square shape of the logo-only image.** For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including additional padding.
> 마스크를 사용하여 로고 전용 이미지의 기본 사각형 모양을 변경합니다. 예를 들어 원형 또는 둥근 직사각형 모양을 사용하여 모든 로고 전용 로그인 단추를 표시할 수 있습니다. 내장된 패딩을 줄이거나 로고를 직접 사용하기 위해 Apple에서 제공하는 아트워크를 자르지 말고 추가 패딩을 포함하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-masked-rounded-rect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-masked-rounded-rect_2x.png)

Rounded rectangle mask

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-default_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-default_2x.png)

No mask

![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-masked-circle_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/logo-masked-circle_2x.png)

Circular mask

**Maintain a minimum margin around the button.** The margin should measure at least 1/10 of the button’s height.
> 버튼 주위의 최소 여백을 유지합니다. 여백은 버튼 높이의 10분의 1 이상이어야 합니다.
>



