---
title: ITBLCrosshairInterface
type: class
aliases: ITBLCrosshairInterface
share: false

---

# ITBLCrosshairInterface





Inherits from IInterface

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CrosshairDamageEvent]]**(FName Event, const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent, bool IsEnemy) |
| void | **[[CrosshairDamageTakenEvent]]**(float Damage, float HitDirection) |
| void | **[[CrosshairGameplayEvent]]**(FName Event, bool Enable, float Scaling, bool IsPositive) |
| void | **[[CrosshairHoldingAborted]]**(bool IsStateEnd, bool Force) |
| void | **[[CrosshairHoldingCompleted]]**() |
| void | **[[CrosshairHoldingInitiated]]**(bool IsRangedAttack) |
| void | **[[CrosshairHoldingProgress]]**(float Progress) |
| void | **[[CrosshairLostLimbMessage]]**() |
| void | **[[CrosshairOutOfCombatWarning]]**(bool bShowMessage) |
| void | **[[CrosshairPostRespawnMessage]]**(const FText & ClassName) |
| void | **[[CrosshairPostShuffleMessage]]**() |
| void | **[[CrosshairProjectileFired]]**() |
| void | **[[CrosshairTutorialFailedMessage]]**(const FText & CustomText) |
| void | **[[CrosshairTutorialNeutralMessage]]**(const FText & CustomText) |
| void | **[[CrosshairTutorialSuccessMessage]]**(const FText & CustomText) |
| void | **[[CrosshairWasParried]]**() |
| void | **[[EnableCombatCondition]]**(const FString & Keybinding, FName Condition, bool Enable, const FText & HintText) |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200