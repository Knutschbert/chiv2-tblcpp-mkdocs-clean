---
title: UPartyList
type: class
aliases: UPartyList
share: false

---

# UPartyList





Inherits from [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), UUserWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UPartyList]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[InitPartyWidget]]**() |
| bool | **[[IsPlayingMenu]]**() |
| void | **[[OnFriendsUpdated]]**(const TSet< FString > & ChangedUsers) |
| void | **[[OnPostLoadMap]]**(UWorld * LoadedWorld) |
| void | **[[OnVOIPTick]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UPartyListEntry](/docs/SDK/Source/Classes/classUPartyListEntry.md) * > | **[[EntryWidgets]]**  |
| TMap< FString, [UPartyListEntry](/docs/SDK/Source/Classes/classUPartyListEntry.md) * > | **[[IdToEntryMap]]**  |
| UOverlay * | **[[InviteButtonOverlay]]**  |
| uint8 | **[[MaxPartySize]]**  |
| UVerticalBox * | **[[PartyList]]**  |
| TSubclassOf< [UPartyListEntry](/docs/SDK/Source/Classes/classUPartyListEntry.md) > | **[[PartyListEntryClass]]**  |
| UVerticalBox * | **[[PartyWidgetContainer]]**  |
| [UPartyListEntry](/docs/SDK/Source/Classes/classUPartyListEntry.md) * | **[[SelfPartyEntry]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200