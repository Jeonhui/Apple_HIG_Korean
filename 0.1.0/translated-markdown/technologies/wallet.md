# **[technologies] wallet**

# Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.
> 지갑은 사람들이 신용카드와 직불카드, 운전면허증이나 신분증, 교통카드, 이벤트 티켓, 열쇠 등을 아이폰과 애플워치에 안전하게 저장할 수 있도록 도와준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png)

People use their cards and passes in Wallet to make Apple Pay — and Apple Pay Later — purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.
> 사람들은 애플 페이(Apple Pay)와 애플 페이 라이터(Apple Pay Later)를 구매하고, 주문을 추적하고, 신원을 확인하며, 비행기 탑승, 콘서트 참석 또는 할인과 같은 활동을 간소화하기 위해 자신의 카드와 패스를 사용합니다.
>




When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can access personal content, and offer detailed receipts and tracking information where it’s most convenient. For developer guidance, see [Wallet](https://developer.apple.com/documentation/passkit/wallet).
> Apple Wallet을 앱에 통합하면 사용자 지정 패스를 생성하여 필요한 순간에 제시하고, 개인 컨텐츠에 액세스할 수 있도록 개인의 신원을 안전하게 확인하고, 가장 편리한 곳에서 상세한 영수증 및 추적 정보를 제공할 수 있습니다. 개발자 지침은 지갑을 참조하십시오.
>




# **Passes**

**Offer to add new passes to Wallet.** When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap (for developer guidance, see [addPasses(_:withCompletionHandler:)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)). If people want to review a pass before adding it, you can display a custom view that displays the pass and provides an Add to Apple Wallet button; for developer guidance, see [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller).
> 사람들이 비행기 탑승 수속, 이벤트 티켓 구입, 상점 보상 프로그램 등록 등 새로운 패스를 할 때 한 번의 탭으로 월렛에 패스를 추가할 수 있는 시스템 제공 UI를 제시할 수 있습니다(개발자 지침은 패스 추가(_:CompletionHandler:)). 사용자가 패스를 추가하기 전에 확인하려는 경우 패스를 표시하고 Apple Wallet에 추가 단추를 제공하는 사용자 정의 뷰를 표시할 수 있습니다. 개발자 지침은 PKAddPassesViewController를 참조하십시오.
>




**Help people add a pass that they created outside of your app.** If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.
> 다른 사람들이 당신의 앱 밖에서 만든 패스를 추가할 수 있도록 도와줍니다. 만약 사람들이 당신의 웹사이트나 다른 기기를 사용하여 패스를 만든다면, 그들이 다음에 당신의 앱을 열 때 지갑에 그것을 추가할 것을 제안합니다. 만약 사람들이 당신의 제안을 거절한다면, 그들에게 다시 묻지 마세요.
>




**Add related passes as a group.** If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don’t have to add each one individually. If people can receive a group of passes from your website — such as a set of tickets for an event — bundle them together so that people can download all of them at one time. For developer guidance, see [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing_and_updating_a_pass).
> 단체로 관련 패스를 추가합니다. 다중 연결 항공편의 탑승권과 같이 앱에서 여러 개의 패스를 생성하는 경우, 사람들이 개별적으로 추가할 필요가 없도록 모든 패스를 동시에 추가하십시오. 이벤트 티켓 세트와 같은 사용자가 웹 사이트에서 패스 그룹을 받을 수 있는 경우 한 번에 모든 패스를 다운로드할 수 있도록 패스 그룹을 함께 묶습니다. 개발자 지침은 패스 배포 및 업데이트를 참조하십시오.
>




**Display an Add to Apple Wallet button to let people add an existing pass that isn’t already in Wallet.** If people previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add it if they change their minds. You can display an Add to Apple Wallet button wherever the corresponding pass information appears in your app. For developer guidance, see [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton). You can also display an Add to Apple Wallet badge in an email or on a webpage; for guidance, see [Add to Apple Wallet guidelines](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).
> 아직 지갑에 없는 기존 패스를 추가할 수 있도록 하려면 Apple Wallet에 추가 단추를 표시합니다. 이전에 다른 사람이 지갑에 패스를 추가하라는 사용자의 제안을 거부했거나 패스를 제거한 경우 단추를 누르면 마음이 바뀌어도 쉽게 추가할 수 있습니다. Apple Wallet에 추가 버튼은 해당 패스 정보가 앱에 표시되는 곳마다 표시할 수 있습니다. 개발자 지침은 PKAddPassButton을 참조하십시오. 전자 메일이나 웹 페이지에 Apple Wallet에 추가 배지를 표시할 수도 있습니다. 자세한 내용은 Apple Wallet에 추가 지침을 참조하십시오.
>




**Let people jump from your app to their pass in Wallet.** Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”
> 사람들이 당신의 앱에서 지갑의 그들의 패스로 점프할 수 있게 해주세요. 당신의 앱이 지갑에 존재하는 패스에 대한 정보를 표시하는 곳이라면, 당신은 그것을 직접 여는 링크를 제공할 수 있습니다. 링크에 "지갑에서 보기"와 같은 레이블을 지정합니다
>




**Consider hiding expired passes.** In iOS 15 and later, Wallet automatically hides expired passes to reduce crowding, while also providing a button that lets people revisit them. To ensure the system hides passes appropriately, set the expiration date, relevant date, and voided properties of each pass correctly; for developer guidance, see [Pass](https://developer.apple.com/documentation/walletpasses/pass/).
> 만료된 패스를 숨기는 것을 고려해보세요. iOS 15 이상에서는 Wallet이 만료된 패스를 자동으로 숨겨서 혼잡을 줄이는 동시에 다시 방문할 수 있는 버튼을 제공합니다. 시스템이 패스를 적절하게 숨기려면 각 패스의 만료 날짜, 관련 날짜 및 무효 속성을 올바르게 설정하십시오. 개발자 지침은 패스를 참조하십시오.
>




**Always get people’s permission before deleting a pass from Wallet.** For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or have them removed automatically. If necessary, you can display an alert before deleting a pass.
> 수동으로 패스를 삭제할지 또는 자동으로 삭제할지 여부를 지정할 수 있는 앱 내 설정을 포함할 수 있습니다. 필요한 경우 패스를 삭제하기 전에 경고를 표시할 수 있습니다.
>




**Help the system suggest a pass on the Lock Screen when it’s contextually relevant.** Ideally, passes automatically appear when they’re needed so people don’t have to manually locate them. When you supply information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it. For example, a gym membership card could appear on the Lock Screen as people enter the gym. For developer guidance, see [Showing a pass on the Lock Screen](https://developer.apple.com/documentation/walletpasses/pass/showing_a_pass_on_the_lock_screen/).
> 시스템에서 잠금 화면에 대한 패스를 제안할 수 있도록 도와줍니다. 패스가 필요할 때 자동으로 나타나므로 수동으로 패스를 찾을 필요가 없습니다. 언제 어디서 패스와 관련된 정보를 제공하면, 사람들이 가장 원할 때 시스템이 해당 패스에 대한 링크를 잠금 화면에 표시할 수 있습니다. 예를 들어, 사람들이 체육관에 들어갈 때 체육관 회원 카드가 잠금 화면에 나타날 수 있습니다. 개발자 지침은 잠금 화면에 패스 표시를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png)

**Update passes as needed.** Physical passes don’t typically change, but a digital pass should reflect updates to events. An airline boarding pass, for example, should automatically update to display flight delays and gate changes.
> 물리적 패스는 일반적으로 변경되지 않지만 디지털 패스는 이벤트에 대한 업데이트를 반영합니다. 예를 들어, 항공사 탑승권은 자동으로 비행 지연과 게이트 변경을 표시하도록 업데이트되어야 한다.
>




**Use change messages only for updates to time-critical information.** A change message interrupts the user’s current workflow, so it’s essential to send one only when you make an update that people must know about. For example, people need to know when there’s a gate change in a boarding pass, but they don’t need to know when a customer service phone number changes. Never use a change message for marketing or other noncritical communication. You enable change messages on a per-field basis; for developer guidance, see [Adding a web service to update passes](https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes/).
> 변경 메시지는 시간이 중요한 정보에 대한 업데이트에만 사용하십시오. 변경 메시지는 사용자의 현재 워크플로우를 중단하므로 사용자가 알아야 할 업데이트를 할 때만 메시지를 전송해야 합니다. 예를 들어 탑승권에 게이트 변경이 있을 때는 알아야 하지만 고객 서비스 전화번호가 변경될 때는 알 필요가 없습니다. 마케팅이나 기타 중요하지 않은 커뮤니케이션을 위해 변경 메시지를 사용하지 마십시오. 필드별로 변경 메시지를 사용할 수 있습니다. 개발자 지침은 업데이트 패스에 웹 서비스 추가를 참조하십시오.
>




# **Designing passes**

Wallet uses a consistent design aesthetic to strengthen familiarity and build trust. Instead of merely replicating the appearance of a physical item, design a clean, simple pass that looks at home in Wallet.
> 지갑은 일관된 디자인 미학을 사용하여 친숙함을 강화하고 신뢰를 쌓는다. 단순히 실제 항목의 모양을 복제하는 대신 지갑에서 집을 볼 수 있는 깨끗하고 간단한 패스를 설계하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png)

**Design a pass that looks great and works well on all devices.** Passes can look different on different devices. For example, when a pass appears on Apple Watch, it doesn’t display all the images it displays when it appears on iPhone (for guidance, see [Passes for Apple Watch](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes-for-apple-watch)). Don’t put essential information in elements that might be unavailable on certain devices. Also, don’t add padding to images; for example, watchOS crops white space from some images.
> 보기 좋고 모든 장치에서 잘 작동하는 패스를 설계하십시오. 패스는 장치마다 다르게 보일 수 있습니다. 예를 들어 Apple Watch에 패스가 표시될 때 iPhone에 표시되는 모든 이미지가 표시되지는 않습니다(자세한 내용은 Apple Watch용 패스 참조). 특정 장치에서 사용할 수 없는 요소에는 필수 정보를 넣지 마십시오. 또한 이미지에 패딩을 추가하지 마십시오(예: 보기)OS는 일부 이미지에서 빈 공간을 잘라냅니다.
>




**Avoid using device-specific language.** You can’t predict the device people will use to view your pass, so don’t include copy that might not make sense on a particular device. For example, copy that tells people to “slide to view” content doesn’t make sense when it appears on Apple Watch.
> 장치별 언어를 사용하지 마십시오. 사람들이 사용자의 패스를 볼 때 사용할 장치를 예측할 수 없으므로 특정 장치에서 의미가 없는 복사본을 포함하지 마십시오. 예를 들어, 사람들에게 내용을 "보기 위해 슬라이드"하라고 말하는 복사본은 Apple Watch에 표시될 때 의미가 없습니다.
>




**Make your pass instantly identifiable.** Using color — especially a color that’s linked to your brand — can help people recognize your pass as soon as they see it. Make sure that pass content remains comfortably readable against the background you choose.
> 색상(특히 브랜드와 연결된 색상)을 사용하면 사람들이 사용자의 패스를 보자마자 인식할 수 있습니다. 통과 내용이 선택한 배경에서 편안하게 읽을 수 있는지 확인합니다.
>




**Keep the front of a pass uncluttered so people can get important information at a glance.**Show essential information — like an event date or account balance — in the top-right area of the pass so people can still see it when the pass is collapsed in Wallet. Use the rest of the pass front to provide important information; consider putting extra information on the back of a pass (iOS) or in a details screen (watchOS).
> 사람들이 한 눈에 중요한 정보를 얻을 수 있도록 통행증 앞을 어질러 놓지 마세요.이벤트 날짜 또는 계정 잔액과 같은 필수 정보를 패스의 오른쪽 상단 영역에 표시하여 패스가 Wallet에서 축소되어도 계속 볼 수 있도록 합니다. 중요한 정보를 제공하려면 패스 프론트의 나머지 부분을 사용하십시오. 패스 뒷면(iOS) 또는 상세 화면(워치OS)에 추가 정보를 넣는 것을 고려하십시오.
>




**Prefer an NFC-enabled pass.** People appreciate having a contactless pass, because it means that they can just hold their device near a reader. If you support both NFC and a barcode or QR code, the code appears on the back of the pass (in iOS) or in the details screen (in watchOS). In iOS, you can display a QR code or barcode on the front of your pass if necessary for your design.
> 근거리 무선 통신이 가능한 패스를 선호한다. 사람들은 비접촉식 패스를 갖는 것을 좋아한다. 왜냐하면 그것은 그들이 그들의 기기를 리더기 근처에 둘 수 있다는 것을 의미하기 때문이다. NFC와 바코드 또는 QR 코드를 모두 지원하는 경우, 코드는 패스 뒷면(iOS)이나 세부 정보 화면(watchOS)에 나타납니다. iOS에서는 디자인에 필요한 경우 QR 코드나 바코드를 패스 앞면에 표시할 수 있습니다.
>




**Reduce image sizes for optimal performance.** People can receive passes via email or a webpage. To make downloads as fast as possible, use the smallest image files that still look great.
> 최적의 성능을 위해 이미지 크기를 줄입니다. 사람들은 이메일이나 웹페이지를 통해 패스를 받을 수 있습니다. 가능한 한 빨리 다운로드하려면 보기 좋은 최소 이미지 파일을 사용하십시오.
>




**Provide an icon that represents your company or brand.** The system includes your icon when displaying information about a relevant pass on the lock screen. Mail also uses the icon to represent your pass in an email message. You can use your app icon or design an icon for this purpose. Create an icon that measures a minimum of 38x38 pts.
> 회사 또는 브랜드를 나타내는 아이콘을 제공하십시오. 시스템은 잠금 화면에 관련 패스에 대한 정보를 표시할 때 아이콘을 포함합니다. 메일은 또한 전자 메일 메시지에서 사용자의 암호를 나타내기 위해 아이콘을 사용합니다. 이를 위해 앱 아이콘을 사용하거나 아이콘을 디자인할 수 있습니다. 최소 38x38ppt을 측정하는 아이콘을 만듭니다.
>




The system defines several pass *styles*, each of which specifies the overall appearance of a pass in categories like event ticket, boarding pass, and coupon. The pass style determines the layout of your content, and can affect the types of relevancy information you provide (for guidance, see [Passes](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes)).
> 시스템은 이벤트 티켓, 탑승권 및 쿠폰과 같은 범주에서 패스의 전체적인 모양을 지정하는 여러 개의 패스 스타일을 정의합니다. 통과 유형은 내용의 레이아웃을 결정하며, 제공하는 관련 정보 유형에 영향을 미칠 수 있습니다(참고 사항은 통과 참조).
>




Although each pass style is different, all styles display information using the basic layout areas shown below:
> 각 통과 스타일은 다르지만, 모든 스타일은 아래에 표시된 기본 레이아웃 영역을 사용하여 정보를 표시합니다:
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png)

All passes display a logo image; depending on style, passes can display additional images in other areas. To display text, you use the following [pass fields](https://developer.apple.com/documentation/walletpasses/passfields) to provide content within specific layout areas:
> 모든 패스는 로고 이미지를 표시합니다. 스타일에 따라 패스는 다른 영역에 추가 이미지를 표시할 수 있습니다. 텍스트를 표시하려면 다음 암호 필드를 사용하여 특정 레이아웃 영역 내에서 내용을 제공합니다:
>




| Field | Layout area | Use to provide... |
| --- | --- | --- |
| Header | Essential | Critical information that should remain visible when the pass is collapsed in Wallet. |
| Primary | Primary | Important information that helps people use the pass. |
| Secondary and auxiliary | Secondary and auxiliary | Useful information that people might not need every time they use the pass. |
| Back | Not shown in diagram | Supplemental details that don’t need to be on the pass front. |

In general, a pass can have up to three header fields, one primary field, up to four secondary fields, and up to four auxiliary fields. Depending on the amount of content you display in each field, some fields may not be visible.
> 일반적으로 패스는 최대 3개의 헤더 필드, 1개의 기본 필드, 4개의 보조 필드 및 4개의 보조 필드를 가질 수 있습니다. 각 필드에 표시하는 내용의 양에 따라 일부 필드가 표시되지 않을 수 있습니다.
>




**Display text only in pass fields.** The system ensures that text in pass fields is legible and accessible to assistive technologies like VoiceOver. Don’t embed text in images — it’s not accessible and not all images are displayed on all devices — and avoid using custom fonts that might make text hard to read.
> 암호 필드에만 텍스트를 표시합니다. 이 시스템은 암호 필드의 텍스트를 읽을 수 있고 VoiceOver와 같은 보조 기술에 액세스할 수 있도록 보장합니다. 이미지에 텍스트를 포함하지 마십시오. 액세스할 수 없고 일부 이미지가 모든 장치에 표시되지 않습니다. 또한 텍스트를 읽기 어렵게 만들 수 있는 사용자 지정 글꼴을 사용하지 마십시오.
>




# **Boarding passes**

Use the boarding pass style for train tickets, airline boarding passes, and other types of transit passes. Typically, each pass corresponds to a single trip with a specific starting and ending point.
> 기차표, 항공사 탑승권 및 기타 유형의 환승권에는 탑승권 스타일을 사용합니다. 일반적으로 각 패스는 특정 시작점과 종료점이 있는 단일 트립에 해당합니다.
>




A boarding pass can display logo and footer images, and it can have up to two primary fields and up to five auxiliary fields.
> 탑승권은 로고 및 바닥글 이미지를 표시할 수 있으며, 최대 2개의 기본 필드와 최대 5개의 보조 필드를 가질 수 있습니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png)


# **Coupons**

Use the coupon style for coupons, special offers, and other discounts. A coupon can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 쿠폰, 특별 할인 및 기타 할인에 쿠폰 스타일을 사용합니다. 쿠폰은 로고와 스트립 이미지를 표시할 수 있으며, 한 행에 표시되는 보조 및 보조 필드를 최대 4개까지 포함할 수 있습니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png)


# **Store cards**

Use the store card style for store loyalty cards, discount cards, points cards, and gift cards. If an account related to a store card carries a balance, the pass usually shows the current balance.
> 상점 충성도 카드, 할인 카드, 포인트 카드 및 기프트 카드에 상점 카드 스타일을 사용합니다. 매장 카드와 관련된 계좌에 잔액이 있을 경우, 패스는 보통 현재 잔액을 보여준다.
>




A store card can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 상점 카드는 로고 및 스트립 이미지를 표시할 수 있으며 최대 4개의 보조 및 보조 필드를 가질 수 있으며, 모두 한 행에 표시됩니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png)


# **Event tickets**

Use the event ticket style to give people entry into events like concerts, movies, plays, and sporting events. Typically, each pass corresponds to a specific event, but you can also use a single pass for several events, as with a season ticket.
> 이벤트 티켓 스타일을 사용하여 사람들에게 콘서트, 영화, 연극 및 스포츠 이벤트와 같은 이벤트에 입장할 수 있습니다. 일반적으로 각 패스는 특정 이벤트에 해당하지만 시즌 티켓과 같이 여러 이벤트에 대해 단일 패스를 사용할 수도 있습니다.
>




An event ticket can display logo, strip, background, or thumbnail images. However, if you supply a strip image, don’t include a background or thumbnail image. You can also include an extra row of up to four auxiliary fields (for developer guidance, see the `row` property of [PassFields.AuxiliaryFields](https://developer.apple.com/documentation/walletpasses/passfields/auxiliaryfields)).
> 이벤트 티켓은 로고, 스트립, 배경 또는 썸네일 이미지를 표시할 수 있습니다. 그러나 스트립 이미지를 제공하는 경우 배경 또는 축소 이미지를 포함하지 마십시오. 최대 4개의 보조 필드 행을 추가로 포함할 수도 있습니다(개발자 지침은 PassFields의 '행' 속성 참조).보조 필드).
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png)


# **Generic passes**

Use the generic style for a type of pass that doesn’t fit into the other categories, such as a gym membership card or coat-check claim ticket. A generic pass can display logo and thumbnail images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 체육관 회원 카드 또는 코트 체크 청구권과 같은 다른 범주에 맞지 않는 유형의 패스에 일반적인 스타일을 사용합니다. 일반 패스는 로고 및 섬네일 이미지를 표시할 수 있으며, 최대 4개의 보조 및 보조 필드를 가질 수 있으며, 모두 한 행에 표시됩니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png)


# **Passes for Apple Watch**

On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.
> Apple Watch에서 Wallet은 카드의 회전식 회전대에 패스를 표시합니다. 시계 전용 앱을 만들지 않아도 Apple Watch에 사용자의 패스를 추가할 수 있으므로 단말기에서 사용자의 패스가 어떻게 표시되는지 이해하는 것이 중요합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png)

On their Apple Watch, people can tap a card to reveal a details screen that displays additional pass information in a scrolling view. In some cases, people can also tap a specific transaction to get more information.
> 애플 워치에서 사람들은 카드를 눌러 스크롤 뷰에 추가 패스 정보를 표시하는 세부 화면을 표시할 수 있다. 경우에 따라, 사람들은 더 많은 정보를 얻기 위해 특정 거래를 탭 할 수도 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png)

Each pass style specifies the fields and images that can appear in the basic layout areas shown below:
> 각 통과 스타일은 아래에 표시된 기본 레이아웃 영역에 나타날 수 있는 필드와 이미지를 지정합니다:
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png)

If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.
> 일부 정보가 레이아웃 영역에 맞지 않으면 시스템이 스크롤 세부 정보 화면에 표시합니다.
>




**IMPORTANT**In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.
> 모든 스타일에서 중요, 주의OS는 스트립 이미지를 카드 인터페이스의 가로 세로 비율에 맞게 잘라내고 다른 이미지에서 공백을 잘라낼 수 있습니다.
>




• [Boarding](../technologies/wallet#)
• [Coupon](../technologies/wallet#)
• [Store](../technologies/wallet#)
• [Event](../technologies/wallet#)
• [Generic](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png)


# **Order tracking**

When you support Order Tracking, Wallet can automatically display information about an order after people successfully complete an Apple Pay purchase through your app or website, updating the information whenever the status of the order changes.
> 주문 추적을 지원하는 경우, Wallet은 앱 또는 웹 사이트를 통해 Apple Pay 구매를 성공적으로 완료한 후 주문에 대한 정보를 자동으로 표시하여 주문 상태가 변경될 때마다 정보를 업데이트할 수 있습니다.
>




Wallet presents a dashboard that displays a customer’s active and completed orders. People can choose an order to view details about it, like the items they ordered and fulfillment information for shipping and pickup.
> Wallet은 고객의 활성 주문과 완료된 주문을 표시하는 대시보드를 제공합니다. 주문을 선택하여 주문한 품목과 배송 및 픽업에 대한 배송 정보와 같은 세부 정보를 볼 수 있습니다.
>




The [Wallet Orders](https://developer.apple.com/documentation/walletorders) schema defines the fields you use to provide order data like product descriptions, order status, contact information, and shipping and pickup details, including estimated arrival dates, addresses, tracking numbers, and pickup instructions. Wallet displays the information you supply within consistent, system-defined interfaces. To help people get the information they need quickly and conveniently, supply as much information as you can, using the fields that match your order processes.
> 지갑 주문 스키마는 제품 설명, 주문 상태, 연락처 정보, 예상 도착 날짜, 주소, 추적 번호 및 픽업 지침을 포함한 배송 및 픽업 세부 정보와 같은 주문 데이터를 제공하는 데 사용하는 필드를 정의합니다. 지갑은 일관된 시스템 정의 인터페이스 내에서 사용자가 제공하는 정보를 표시합니다. 사람들이 필요한 정보를 빠르고 편리하게 얻을 수 있도록 주문 프로세스와 일치하는 필드를 사용하여 가능한 한 많은 정보를 제공하십시오.
>




**Make data available immediately after people place an order.** People often want to confirm that their order was received, even when payment, processing, and fulfillment are still pending. It’s essential to provide existing information quickly so that the system can display it right away.
> 주문 후 즉시 데이터를 사용할 수 있도록 합니다. 결제, 처리 및 이행이 보류 중인 경우에도 주문이 접수되었는지 확인하려는 경우가 많습니다. 시스템이 바로 표시할 수 있도록 기존 정보를 신속하게 제공하는 것이 필수적이다.
>




**Provide fulfillment information as soon as it’s available, and keep the status up to date.**When you supply fulfillment data or you change the status of an order, the system updates the order information and can automatically send a notification to customers. The system uses the fulfillment status you report to update the order’s current status to a value like Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, or — if something goes wrong — Issue or Canceled. For guidance on describing a status, see [Displaying order and fulfillment details](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#displaying-order-and-fulfillment-details).
> 사용 가능한 즉시 이행 정보를 제공하고 상태를 최신 상태로 유지합니다.이행 데이터를 제공하거나 주문 상태를 변경하면 시스템이 주문 정보를 업데이트하고 고객에게 자동으로 알림을 보낼 수 있습니다. 시스템은 사용자가 보고한 이행 상태를 사용하여 주문의 현재 상태를 주문 완료, 처리, 픽업 준비, 픽업, 배달, 배달 등의 값으로 업데이트하거나 문제가 발생할 경우 발급 또는 취소와 같은 값으로 업데이트합니다. 상태 설명에 대한 지침은 주문 및 이행 세부사항 표시를 참조하십시오.
>




**Supply a high-resolution logo image.** The system displays your logo image in the dashboard and detail view, so you want to make sure that people can instantly recognize it at various sizes. Use the PNG or JPEG format to create a logo image that measures 300x300 pixels. For developer guidance, see [logo](https://developer.apple.com/documentation/walletorders/merchant).
> 고해상도 로고 이미지를 제공합니다. 이 시스템은 대시보드 및 세부 정보 보기에 로고 이미지를 표시하므로 다양한 크기로 즉시 인식할 수 있습니다. PNG 또는 JPEG 형식을 사용하여 300x300픽셀의 로고 이미지를 만듭니다. 개발자 지침은 로고를 참조하십시오.
>




**Supply distinct, high-resolution product images.** The system displays a product’s image — along with descriptive information you supply — in the detail views, order dashboard, and notifications for an order or a fulfillment. When creating a product image, prefer using a straightforward depiction and a solid background. Showing a product in a “lifestyle” context or against a busy background can make the item hard to distinguish at small sizes. For each product, use the PNG or JPEG format to create an image that measures 300x300 pixels.
> 고유한 고해상도 제품 이미지를 제공합니다. 시스템은 사용자가 제공하는 설명 정보와 함께 제품 이미지를 상세 보기, 주문 대시보드 및 주문 또는 이행에 대한 알림에 표시합니다. 제품 이미지를 만들 때는 간단한 묘사와 확실한 배경을 사용하는 것이 좋습니다. "라이프스타일" 맥락에서 또는 바쁜 배경에서 제품을 보여주면 작은 크기에서 제품을 구분하기 어려울 수 있다. 각 제품에 대해 PNG 또는 JPEG 형식을 사용하여 300x300픽셀을 측정하는 이미지를 만듭니다.
>




**In general, keep text brief.** People appreciate being able to read text at a glance, and the system can truncate text that’s too long.
> 일반적으로 텍스트를 짧게 유지하십시오. 사람들은 텍스트를 한 눈에 볼 수 있는 것을 좋아하고 시스템은 너무 긴 텍스트를 잘라낼 수 있습니다.
>




**Use clear, approachable language, and localize the text you provide.** You want to make sure that all your customers can read the information in an order. Also, make sure the price you show matches the final price the customer confirmed.
> 명확하고 쉽게 접근할 수 있는 언어를 사용하고 제공하는 텍스트를 현지화하십시오. 모든 고객이 주문의 정보를 읽을 수 있도록 하려는 것입니다. 또한 당신이 보여주는 가격이 고객이 확인한 최종 가격과 일치하는지 확인하십시오.
>




# **Displaying order and fulfillment details**
> 주문 및 이행내역 표시
>




An order gives people ways to contact you and displays details about their Apple Pay purchase, including fulfillment status and per-item information.
> 주문은 사용자에게 연락할 수 있는 방법을 제공하며, 이행 상태 및 항목별 정보를 포함하여 Apple Pay 구매에 대한 세부 정보를 표시합니다.
>




**Provide a link to an area where people manage their order.** When you provide a universal link, people can open your order management area even if they don’t have your app installed. To learn more about universal links, see [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?preferredLanguage=occ); for developer guidance, see [orderManagementURL](https://developer.apple.com/documentation/walletorders/order).
> 사용자가 주문을 관리하는 영역에 대한 링크를 제공합니다. 범용 링크를 제공하면 사용자의 앱이 설치되어 있지 않더라도 주문 관리 영역을 열 수 있습니다. 범용 링크에 대한 자세한 내용은 앱 및 웹 사이트의 콘텐츠 연결 허용을 참조하십시오.개발자 지침은 주문 관리를 참조하십시오URL.
>




**Clearly describe each item so people can verify that their order contains everything they expect.** You can use the [lineItem](https://developer.apple.com/documentation/walletorders/lineitem) field to provide information like a product’s price, name, and image. An order lists the line items for every item the customer ordered; a fulfillment lists only the line items that fulfillment includes.
> 사람들이 그들의 주문이 그들이 기대하는 모든 것을 포함하고 있는지 확인할 수 있도록 각 품목을 명확하게 설명하십시오. lineItem 필드를 사용하여 제품의 가격, 이름 및 이미지와 같은 정보를 제공할 수 있습니다. 주문에는 고객이 주문한 모든 품목의 라인 항목이 나열되고, 풀필먼트에는 풀필먼트가 포함된 라인 항목만 나열됩니다.
>




**Supply a prioritized list of your apps that might be installed on the device.** The system uses this list when it needs to display a link to your app within the order details view. For example, if you provide multiple apps and more than one of them is installed on the device, the system displays a link to the installed app that’s highest on your list. If none of your apps are installed on the device, the system displays a link to the first app on your list. For developer guidance, see [associatedApplications](https://developer.apple.com/documentation/walletorders/order).
> 장치에 설치될 수 있는 앱의 우선 순위 목록을 제공하십시오. 시스템은 주문 세부 정보 보기 내에 앱에 대한 링크를 표시해야 할 때 이 목록을 사용합니다. 예를 들어, 여러 개의 앱을 제공하고 두 개 이상의 앱이 장치에 설치되어 있는 경우 목록에서 가장 높은 위치에 있는 설치된 앱에 대한 링크가 시스템에 표시됩니다. 장치에 설치된 앱이 없는 경우 목록의 첫 번째 앱에 대한 링크가 표시됩니다. 개발자 지침은 관련 응용프로그램을 참조하십시오.
>




**Avoid sending duplicate notifications.** For example, you can tell the system to avoid sending order-related notifications through Wallet when the customer has one of your associated apps installed.
> 중복된 알림을 보내지 않도록 합니다. 예를 들어, 고객이 연결된 앱 중 하나를 설치한 경우 주문 관련 알림을 Wallet을 통해 보내지 않도록 시스템에 지시할 수 있습니다.
>




**Make it easy for customers to contact you.** Provide multiple contact methods, so people can choose the one that works best for them. At minimum, you need to provide a link to your website or landing page, but you can also provide a Messages for Business link, a phone number, an email address, and a link to your support page (for developer guidance, see [Merchant](https://developer.apple.com/documentation/walletorders/merchant)). When people choose the Contact button in an order, the system displays a menu of the contact methods you supply.
> 고객이 쉽게 연락할 수 있도록 합니다. 여러 연락 방법을 제공하여 사람들이 자신에게 가장 적합한 방법을 선택할 수 있도록 합니다. 최소한 웹 사이트 또는 랜딩 페이지에 대한 링크를 제공해야 하지만 비즈니스 메시지 링크, 전화 번호, 이메일 주소 및 지원 페이지에 대한 링크도 제공할 수 있습니다(개발자 지침은 상인 참조). 사용자가 주문에서 연락처 단추를 선택하면 시스템에 사용자가 제공하는 연락처 방법의 메뉴가 표시됩니다.
>




**Help people track their order.** A multi-item order can have multiple fulfillments, where each fulfillment is either shipping or pickup. For example, if a customer orders a pair of shoes and a T-shirt, the customer might want to have one item shipped, while picking up the other. Regardless of fulfillment type, you need to supply enough information for people to know where their items are and when to expect them at the destination they specified. In addition to an estimated time of arrival, here’s some information that people particularly appreciate:
> 사람들이 주문을 추적할 수 있도록 도와줍니다. 여러 항목의 주문에는 배송 또는 픽업이 포함된 여러 가지 주문이 포함될 수 있습니다. 예를 들어, 고객이 신발 한 켤레와 티셔츠를 주문하는 경우, 고객은 한 품목을 배송받으면서 다른 품목을 배송하기를 원할 수 있습니다. 이행 유형에 관계없이, 사용자가 지정한 목적지에서 항목의 위치와 예상 시기를 알 수 있도록 충분한 정보를 제공해야 합니다. 예상 도착 시간 외에도, 사람들이 특히 높이 평가하는 몇 가지 정보가 있습니다:
>




- A link that opens the carrier’s website to a page with information about a shipping fulfillment. When possible, provide a direct link — in addition to a tracking number — so people can easily view the most up-to-date shipping information.
- >  운송업체의 웹 사이트를 열어 배송 완료에 대한 정보가 있는 페이지로 연결하는 링크입니다. 가능한 경우, 사람들이 최신 배송 정보를 쉽게 볼 수 있도록 추적 번호 외에 직접 링크를 제공하십시오.

- A scannable barcode when one is required to pick up the order in a pickup fulfillment. It’s convenient when people can offer the barcode from within Wallet instead of finding it in an email or webpage.
- >  픽업 수행 시 주문을 픽업해야 할 때 스캔 가능한 바코드입니다. 전자 메일이나 웹 페이지에서 바코드를 찾는 대신 지갑 내에서 바코드를 제공할 수 있을 때 편리합니다.

- Clear, detailed instructions that can help people receive or pick up their order.
- >  주문을 받거나 수령하는 데 도움이 될 수 있는 명확하고 상세한 지침.


**Choose shipping-fulfillment values that match the details you have about the shipping process.** If you know the carrier, enter its name in the `carrier` field; otherwise, leave the default “Track Shipment” value. If you can access details about a carrier’s interim shipping steps — such as when a fulfillment is on the way or out for delivery — indicate each step by using specific status values like `onTheWay`, `outForDelivery`, or `delivered`. In contrast, if you don’t have access to a carrier’s shipping details, use the `shipped` status. In both cases, provide a tracking link (when one is available) so people can track their order on their own. For developer guidance, see [ShippingFulfillment](https://developer.apple.com/documentation/walletorders/shippingfulfillment).
> 배송 과정에 대한 세부 정보와 일치하는 배송 완료 값을 선택하십시오. 운송업체를 알고 있는 경우에는 '운송업체' 필드에 이름을 입력하고, 알고 있는 경우에는 기본 '배송 추적' 값을 그대로 둡니다. 운송업체의 중간 배송 단계에 대한 세부 정보에 액세스할 수 있는 경우(예: 배송 중 또는 배송 중인 경우) 'On The Way', 'Out For Delivery' 또는 'delivered'와 같은 특정 상태 값을 사용하여 각 단계를 표시합니다. 반면 운송업체의 배송 정보를 확인할 수 없는 경우에는 배송된 상태를 사용합니다. 두 경우 모두, 사람들이 스스로 주문을 추적할 수 있도록 추적 링크를 제공하십시오. 개발자 지침은 배송 완료를 참조하십시오.
>




**Keep customers informed through relevant fulfillment status descriptions.** A great status message is approachable, accurate, and clearly related to the status it describes. In addition to supplying information that helps people understand the status of their order, a status message also gives you an opportunity to use your brand’s communication style.
> 관련 이행 상태 설명을 통해 고객에게 지속적으로 정보를 제공합니다. 훌륭한 상태 메시지는 접근 가능하고 정확하며 설명하는 상태와 명확하게 관련되어 있습니다. 상태 메시지는 주문 상태를 이해하는 데 도움이 되는 정보를 제공하는 것 외에도 브랜드의 커뮤니케이션 스타일을 사용할 수 있는 기회를 제공합니다.
>




**Be direct and thorough when describing an Issue or Canceled status.** People generally need to know why there’s a problem and what they can do about it.
> 문제 또는 취소 상태를 설명할 때는 직접적이고 철저해야 합니다. 일반적으로 사람들은 문제가 있는 이유와 문제에 대해 무엇을 할 수 있는지 알아야 합니다.
>




# **Identity verification**

On iPhone running iOS 16 and later, people can store an ID card in Wallet, and later allow an app or App Clip to access information on the card to verify their identity without leaving their current context. For example, a person might need to confirm their identity when they apply for a credit card within their banking app.
> iOS 16 이상을 실행하는 아이폰에서 사람들은 지갑에 신분증을 저장할 수 있으며, 나중에 앱이나 앱 클립이 카드의 정보에 액세스하여 현재 컨텍스트를 떠나지 않고 자신의 신원을 확인할 수 있다. 예를 들어, 한 사람이 그들의 은행 앱에서 신용카드를 신청할 때 그들의 신원을 확인해야 할 수도 있다.
>




**DEVELOPER NOTE**Apple doesn’t create or see the ID documents that people add to Wallet, and when people agree to share identifying information with your app, you receive only encrypted data that isn’t readable on the device. For developer guidance, see [Requesting identity data from a Wallet pass](https://developer.apple.com/documentation/passkit/wallet/requesting_identity_data_from_a_wallet_pass).
> 개발자 참고 Apple은 사람들이 Wallet에 추가하는 ID 문서를 만들거나 보지 않으며, 사람들이 앱과 식별 정보를 공유하기로 동의하면 장치에서 읽을 수 없는 암호화된 데이터만 수신합니다. 개발자 지침은 지갑 패스에서 ID 데이터 요청을 참조하십시오.
>




To help you offer a consistent experience that people can trust, Apple provides a Verify with Wallet button you can use in your app when you need to ask for identify verification. The button reveals a sheet that describes your request and lets people agree to share their information or cancel.
> 신뢰할 수 있는 일관된 경험을 제공할 수 있도록 Apple은 식별 확인을 요청해야 할 때 앱에서 사용할 수 있는 Verify with Wallet 버튼을 제공합니다. 이 단추는 사용자의 요청을 설명하고 사용자가 자신의 정보를 공유하거나 취소하는 데 동의할 수 있는 시트를 표시합니다.
>




**Present a Wallet verification option only when the device supports it.** If the current device can’t return the identify information you request, don’t display a Verify with Apple Wallet button. Be prepared to present a fallback view that offers a different verification method if Verify with Apple Wallet isn’t available; for developer guidance, see [VerifyIdentityWithWalletButton](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton).
> 장치에서 지원하는 경우에만 지갑 확인 옵션을 표시합니다. 현재 장치에서 요청한 식별 정보를 반환할 수 없으면 Apple 지갑으로 확인 단추를 표시하지 마십시오. Apple Wallet으로 확인을 사용할 수 없는 경우 다른 확인 방법을 제공하는 폴백 뷰를 제공할 준비를 하십시오. 개발자 지침은 ID 확인을 참조하십시오지갑 단추로.
>




**Ask for identity information only at the precise moment you need it.** People can be suspicious of a request for personal information if it doesn’t seem to be related to their current action. If your app needs identity verification, for example, wait to ask for this information until people are completing the process or transaction that requires it; don't request verification before people are ready to start the process or when they're simply creating an account.
> 필요한 정확한 순간에만 신원정보를 요구하고, 현재의 행동과 관련이 없는 것 같으면 개인정보 요청을 의심할 수 있다. 예를 들어, 앱에 신원 확인이 필요한 경우, 사용자가 프로세스 또는 트랜잭션을 완료할 때까지 이 정보를 요청할 때까지 기다리십시오. 사용자가 프로세스를 시작할 준비가 되기 전에 또는 단순히 계정을 만들 때 확인을 요청하지 마십시오.
>




**Clearly and succinctly describe the reason you need the information you’re requesting.** You must write copy (called a *purpose string* or *usage description string*) that explains why people need to share identity information with your app. The system displays your purpose string in the verification sheet so people can make an informed decision. Here are a couple of examples:
> 요청하는 정보가 필요한 이유를 명확하고 간결하게 설명하십시오. 앱과 ID 정보를 공유해야 하는 이유를 설명하는 복사본(목적 문자열 또는 사용 설명 문자열이라고 함)을 작성해야 합니다. 시스템은 사용자가 정보에 입각한 결정을 내릴 수 있도록 사용자의 목적 문자열을 확인 시트에 표시합니다. 다음은 몇 가지 예입니다:
>




| To verify... | To support... | Example purpose string |
| --- | --- | --- |
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

For each purpose string, aim for a brief, complete sentence that’s direct, specific, and easy for everyone to understand. Use sentence case, avoid passive voice, and include a period at the end.
> 각 목적 문자열에 대해, 직접적이고 구체적이며 모든 사람이 이해하기 쉬운 짧고 완전한 문장을 목표로 하라. 문장 대소문자를 사용하고 수동적인 음성을 피하고 끝에 마침표를 포함합니다.
>


**Ask only for the data you actually need.** People may lose trust in your app if you ask for more data than you need to complete the current task or action. For example, if you need to ensure that a customer is at least a certain age, use a request that specifies an age threshold; avoid requesting the customer’s current age or birth date. For developer guidance, see [age(atLeast:)](https://developer.apple.com/documentation/passkit/pkidentityelement/3930277-age).
> **실제로 필요한 데이터만 요청하십시오.** 현재 작업이나 작업을 완료하는 데 필요한 것보다 더 많은 데이터를 요청하면 사람들이 앱에 대한 신뢰를 잃을 수 있습니다. 예를 들어, 고객이 특정 연령 이상인지 확인해야 하는 경우 연령 임계값을 지정하는 요청을 사용합니다. 고객의 현재 나이 또는 생년월일은 요청하지 마십시오. 개발자 지침은 [연령(최소:)](https://developer.apple.com/documentation/passkit/pkidentityelement/3930277-age)을 참조하십시오.
> 

**Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you’ll do so.** To help people trust your app, it’s essential to explain how long you might need to keep the personal information they agree to share with you. When you use PassKit APIs to specify a duration — such as a particular period, indefinitely, or only as long as it takes to complete the current verification — the system automatically displays explanatory content in the verification sheet. For developer guidance, see [PKIdentityIntentToStore](https://developer.apple.com/documentation/passkit/pkidentityintenttostore).
> **데이터를 보관할지 여부를 명확히 지정하고 보관해야 할 경우 보관 기간을 지정합니다.** 사용자의 앱을 신뢰할 수 있도록 하려면 사용자가 공유하기로 동의한 개인 정보를 얼마나 오래 보관해야 하는지 설명해야 합니다. PassKit API를 사용하여 특정 기간, 무기한 또는 현재 확인을 완료하는 데 걸리는 기간과 같은 기간을 지정하면 시스템은 자동으로 확인 시트에 설명 내용을 표시합니다. 개발자 지침은 [PKIEntityIntentToStore](https://developer.apple.com/documentation/passkit/pkidentityintenttostore).를 참조하십시오.
> 


**Choose the system-provided verification button that matches your use case and the visual design of your app.** The system provides the following button labels to support various use cases:
> **사용 사례 및 앱의 시각적 디자인과 일치하는 시스템 제공 검증 버튼을 선택하십시오.** 시스템은 다양한 사용 사례를 지원하기 위해 다음과 같은 버튼 레이블을 제공합니다:
> 

[제목 없음](https://www.notion.so/18138785e3b64f23862b051c2f16d51d)

All button labels are also available in a multiline variant that the system automatically uses when horizontal space is constrained. For developer guidance, see [PKIdentityButton.Label](https://developer.apple.com/documentation/passkit/pkidentitybutton/label).
> 모든 버튼 레이블은 수평 공간이 제한될 때 시스템이 자동으로 사용하는 다중 라인 변형으로도 사용할 수 있습니다. 개발자 지침은 [PKIDEntityButton.Label](https://developer.apple.com/documentation/passkit/pkidentitybutton/label)을 참조하십시오.
> 

The verification button always uses white letters on a black background. You can choose the style that includes a light outline if you need to ensure that the button contrasts well with a dark background in your app (for developer guidance, see [PKIdentityButton.Style.blackOutline](https://developer.apple.com/documentation/passkit/pkidentitybutton/style/blackoutline)). In addition, you can use the [cornerRadius](https://developer.apple.com/documentation/passkit/pkidentitybutton/3967461-cornerradius) property to adjust the verification button’s corners to match other related buttons in your interface.
> 확인 버튼은 항상 검은색 배경에 흰색 문자를 사용합니다. 버튼이 앱의 어두운 배경과 잘 대비되도록 하려면 밝은 윤곽선이 포함된 스타일을 선택할 수 있습니다(개발자 지침은 [PKIDEntityButton.style.blackOutline](https://developer.apple.com/documentation/passkit/pkidentitybutton/style/blackoutline)). 또한 [cornerRadius](https://developer.apple.com/documentation/passkit/pkidentitybutton/3967461-cornerradius) 속성을 사용하여 확인 버튼의 모서리를 인터페이스의 다른 관련 버튼과 일치하도록 조정할 수 있습니다.
> 
