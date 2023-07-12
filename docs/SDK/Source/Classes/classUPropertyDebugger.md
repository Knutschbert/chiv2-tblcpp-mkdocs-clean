---
title: UPropertyDebugger
type: class
aliases: UPropertyDebugger
share: false

---

# UPropertyDebugger





Inherits from [UTBLComponent](/docs/SDK/Source/Classes/classUTBLComponent.md), UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[DebugInputChar]]**(const FString & Char) |
| void | **[[DrawDebug]]**(UCanvas * Canvas) |
| void | **[[DrawProperty]]**(UCanvas * Canvas, float & XPos, float & YPos, const FString & PropName, const FString & PropVal) |
| void | **[[OnMovementSync]]**([UMovementDebugger](/docs/SDK/Source/Classes/classUMovementDebugger.md) * MovementDebugger) |
| void | **[[PrintToFile]]**() |
| | **[[UPropertyDebugger]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyFilter]]**(const FString & Text) |
| void | **[[ClearFilter]]**() |
| void | **[[ClientReturnSelectedClass]]**(UStruct * Struct) |
| void | **[[CloseDebugger]]**() |
| void | **[[CreateMenu]]**() |
| void | **[[DisplayDebugScrollDown]]**() |
| void | **[[DisplayDebugScrollReleased]]**() |
| void | **[[DisplayDebugScrollUp]]**() |
| void | **[[FindProperty]]**(const FString & PropName) |
| UStruct * | **[[GetOverrideBaseClass]]**(FName BaseObj) |
| UStruct * | **[[GetOverrideSelectedClass]]**(const [FDebugProperty](/docs/SDK/Source/Classes/structFDebugProperty.md) & Property) |
| bool | **[[HandleFilterText]]**(const FString & Char) |
| void | **[[InitHUD]]**() |
| void | **[[MenuAdd]]**() |
| void | **[[MenuBackSpace]]**() |
| void | **[[MenuClose]]**() |
| void | **[[MenuDelete]]**() |
| void | **[[MenuDownPressed]]**() |
| void | **[[MenuLeft]]**() |
| void | **[[MenuOpen]]**() |
| void | **[[MenuPageDown]]**() |
| void | **[[MenuPageUp]]**() |
| void | **[[MenuReleased]]**() |
| void | **[[MenuRight]]**() |
| void | **[[MenuUpPressed]]**() |
| void | **[[NextProperty]]**() |
| void | **[[OnPossessed]]**(APawn * NewPawn) |
| void | **[[PreviousProperty]]**() |
| void | **[[ServerAddDebugProperty]]**(const [FDebugProperty](/docs/SDK/Source/Classes/structFDebugProperty.md) & Property) |
| void | **[[ServerDeleteDebugProperty]]**(bool bFromEnd) |
| void | **[[ServerEnableReplication]]**(bool bReplicate) |
| void | **[[ServerGetBaseClass]]**(FName BaseObj) |
| void | **[[ServerGetSelectedClass]]**(const [FDebugProperty](/docs/SDK/Source/Classes/structFDebugProperty.md) & Property) |
| void | **[[ServerSetOtherActor]]**(AActor * Other) |
| void | **[[ServerSetOtherCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Other) |
| void | **[[ToggleReplication]]**() |
| void | **[[ToggleShowDebugOther]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| AActor * | **[[OtherActor]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[OtherCharacter]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< UActorComponent * > | **[[ActorComponents]]**  |
| TArray< FName > | **[[AllClassNames]]**  |
| int32 | **[[CurrentHistoryIndex]]**  |
| [FPropertyMenuItem](/docs/SDK/Source/Classes/structFPropertyMenuItem.md) | **[[CurrentMenu]]**  |
| FName | **[[DebugAllOption]]**  |
| TArray< [FDebugProperty](/docs/SDK/Source/Classes/structFDebugProperty.md) > | **[[DebugProperties]]**  |
| int32 | **[[DisplayDebugScrollDir]]**  |
| float | **[[DisplayDebugScrollY]]**  |
| TArray< FString > | **[[HistoryBuffer]]**  |
| UInputComponent * | **[[InputComponent]]**  |
| double | **[[LastInputTime]]**  |
| int32 | **[[MenuDirection]]**  |
| float | **[[MenuHeldTime]]**  |
| UInputComponent * | **[[MenuInputComponent]]**  |
| float | **[[MenuTimer]]**  |
| float | **[[MenuTimerRate]]**  |
| [ATBLHUD](/docs/SDK/Source/Classes/classATBLHUD.md) * | **[[MyHUD]]**  |
| float | **[[OtherCharacterTraceTime]]**  |
| TArray< [FPropertyMenuItem](/docs/SDK/Source/Classes/structFPropertyMenuItem.md) > | **[[PropertiesMenu]]**  |
| TArray< [FPropertyMenuItem](/docs/SDK/Source/Classes/structFPropertyMenuItem.md) > | **[[PropertiesMenuUnfiltered]]**  |
| TArray< FString > | **[[RedoStack]]**  |
| FString | **[[SearchText]]**  |
| [FDebugProperty](/docs/SDK/Source/Classes/structFDebugProperty.md) | **[[SelectedProperty]]**  |
| int32 | **[[SelectedPropertyIndex]]**  |
| TArray< [FPropertyUndoItem](/docs/SDK/Source/Classes/structFPropertyUndoItem.md) > | **[[UndoStack]]**  |
| bool | **[[bFilterEnabled]]**  |
| bool | **[[bReplicateProperties]]**  |
| bool | **[[bShowDebugOther]]**  |
| bool | **[[bShowMenu]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200