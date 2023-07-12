---
title: UTBLLocalMessage
type: class
aliases: UTBLLocalMessage
share: false

---

# UTBLLocalMessage





Inherits from ULocalMessage

Inherited by [UTBLLocalMessageGameplayEvent](/docs/SDK/Source/Classes/classUTBLLocalMessageGameplayEvent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastLocalMessage]]**(UObject * WorldContextObject, TSubclassOf< ULocalMessage > MessageClass, int32 Data, APlayerState * PlayerStateA, APlayerState * PlayerStateB, UObject * Object) |
| void | **[[BroadcastPrivateLocalMessage]]**(APlayerController * PlayerController, TSubclassOf< ULocalMessage > MessageClass, int32 Data, APlayerState * PlayerStateA, APlayerState * PlayerStateB, UObject * Object) |
| int32 | **[[PackData]]**(const uint8 & Byte, const int32 & Value) |
| | **[[UTBLLocalMessage]]**() |
| void | **[[UnpackData]]**(const int32 & Data, uint8 & Byte, int32 & Value) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnMessageReceived]]**(APlayerController * Receiver, int32 Data, APlayerState * PlayerStateA, APlayerState * PlayerStateB, UObject * Object) const |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200