# Lean 4.35.0 実証品質監査記録
## ― 言語・記号に基づく形式化と証明認定の正当性を問う製品検査 ―

- **記録日**：2026-10-20
- **文書状態**：実機監査結果 v0.1／後続試験の状態は追跡対象
- **検査対象**：Lean 4.35.0、Lake 5.0.0、証明項の受理・公理依存・仕様との対応・複数検証器
- **実行環境**：GitHub Actions（Ubuntu 22.04／Lean 4.35.0 固定）、実測は GitHub 上の CI ログと保存済み artifact に基づく
- **検査コード**：[`audits/lean4/run_audit.py`（検査専用ブランチ）](https://github.com/gatchimuchio/cognitive-engineering-foundations/blob/audit/lean-methodology-20261020/audits/lean4/run_audit.py)
- **理論的な問題提起の独立記録**：[形式化の正当性への言語論的監査](../formalization/2026-10-20_formalization-method-legitimacy_ja.md)
- **作業範囲**：公開正本の理論本文を変更せず、本書は実測を別個に記録する。

---

## 1. 製品監査に先立つ、最上位の問い

> 完全性が完全証明されていない文字を操作して
> 形式化したものを完全な証明とする根拠を僕は言っている

上記の問いを、単なる「Lean はどの文字列を受理するか」へ縮小しない。検査したいのは**文字・記号による形式化という方法から、証明の正当性・完全性という認定へ進む根拠がどこにあるか**である。

実測を行う理由は、方法論の根拠を製品の具体的な入力・操作・出力・前提・依存関係に照らして監査するためである。製品の説明書に保証境界が明記されている事実を、その境界設定の正当性の証明として採用しない。

## 2. 再現可能な証拠

**第三次の実測**（検査スクリプトの基本ケースを修正した時点）：

| 項目 | 記録 |
| --- | --- |
| GitHub Actions 実行 | [Run 39343803658](https://github.com/gatchimuchio/cognitive-engineering-foundations/actions/runs/39343803658) |
| 対象コミット | [`4f1cc1ef7ea95a6c6f373b0bf36d5e9b04d16baa`](https://github.com/gatchimuchio/cognitive-engineering-foundations/commit/4f1cc1ef7ea95a6c6f373b0bf36d5e9b04d16baa) |
| 実行状態 | GitHub Actions 全体表示：success（完了） |
| 直接実行した単体ケース | 14 件／14 件が設計した受理・拒否の期待結果と一致 |
| `lake check` | strict=終了0、lax=終了1、incomplete=終了1 |
| `lake check --paranoid` | strict=終了0、lax=終了1、incomplete=終了1。**後者2件で独立検査器の panic あり** |
| 出力証拠 | [保存 artifact #12231237029](https://github.com/gatchimuchio/cognitive-engineering-foundations/actions/runs/39343803658/artifacts/12231237029)（Actions による保存期間は30日設定） |
| artifact ZIP SHA-256 | `5aa2cbbc890bc3943dab2427581ed82fcb8d0b4ebb998bbea1243089e8fc7d6d` |

上記の「success」は、全検査器が正常に期待結果へ到達したという意味ではなかった。詳細ログを精査すると、想定した拒否を終了コードだけで採点する検査スクリプトが、独立検査器の異常終了を見逃していた。

**再検査（第四次）**：その誤判定を防ぐため、`panicked at` を含む異常終了を `REVIEW_REQUIRED_VERIFIER_PANIC` とする判定へ修正した。検査コミットは [`bd39f398f6c3c9d658af722c3ea4dd2ea71b583d`](https://github.com/gatchimuchio/cognitive-engineering-foundations/commit/bd39f398f6c3c9d658af722c3ea4dd2ea71b583d)、追試は [Run 39352462392](https://github.com/gatchimuchio/cognitive-engineering-foundations/actions/runs/39352462392)。

**本書の初回保存時点**、第四次は実行中であり、最終判定は未観測。第三次の成功表示で第四次の結果を代用しない。

## 3. 単体14ケース：観測と工学上の意味

| ID | 操作・試験目的 | 第三次の実測 | 何が確認できたか |
| --- | --- | --- | --- |
| C01 | 通常の算術定理を検査 | 受理 | 当該形式命題の受理 |
| C02 | 誤った要求を採用した証明と、真の要求違反の証明を並置 | **双方受理** | 同一の実装から要求適合と不適合の異なる記述を構成できる。受理のみで要求の正しさは認定できない |
| C03 | `False` を任意公理として採用 | 受理、`falsePremise` 依存が表示 | 公理を前提とした導出と公理自体の正当化は同じではない |
| C04 | `sorry` による未完成証明 | 警告付き受理、`sorryAx` 依存 | 未完成な根拠が残る |
| C05 | 未完成証明を経由して依存 | 警告・`sorryAx` 依存 | 依存が下流へ伝播する |
| C06 | 排中律の使用 | 受理 | 標準的な公理依存の存在 |
| C07 | `1 = 2` を直接 `rfl` で証明 | 拒否 | 当該不正な証明を検出 |
| C08 | 偽となるアクセス要件を直接証明 | 拒否 | 当該要求違反を検出 |
| C09 | `Safety := (true = true)`、`theorem certified : Safety` | 受理 | 定義に依存した証明成立 |
| C10 | `Safety := (true = false)`、`theorem certified : Safety` | 拒否 | **証明側の同一文字列でも、定義の違いで検査結果が変化** |
| C11 | 異なる値を同一コードへ写す符号化 | 受理 | 符号化が元の差異を失っていても、符号化後の命題は正しく検査できる |
| C12 | 差異を保持する符号化 | 受理 | C11 との対照が成立 |
| C13 | 外部に由来する公理 `externallyCertified` を導入 | 受理 | 証明結果が採用した前提に依存する |
| C14 | `allSymbolsComplete : Prop := True` の定理 | 受理 | 記号への「完全性」の命名が、それ自体で表現手段の完全性を保証するわけではない |

C02・C09～C14は**形式化によって何を検査対象として立てたか**という問題に照準を合わせた試験であり、別資料に記録した上位の言語論的監査質問へ接続する。実測が示すのは、この入力群についての振る舞いである。

## 4. Lake 検査の重要ログ：成功・拒否・異常終了

第三次の artifact に残された実測出力の抜粋。

**標準条件（strict）での `lake check`：**

```text
Running Lean default kernel on solution
Lean default kernel accepts the solution
Uses axioms: Classical.choice, propext, Quot.sound
```

**strict での `lake check --paranoid`：** Lean paranoid、lean4lean、nanoda、con-leche、con-ron、Lean default の各検査器が受理した（終了コード0）。

**任意公理を導入した場合（lax）：**

```text
error: Axiom 'falsePremise' is not permitted; it is used by 'arbitraryEquality'
```

**未完成証明がある場合（incomplete）：**

```text
warning: Incomplete.lean:1:8: declaration uses `sorry`
error: Axiom 'sorryAx' is not permitted; it is used by 'unprovedClaim'
```

**重要な異常終了（第三次の `--paranoid` の lax / incomplete）：**

```text
thread 'thread_3' (6) panicked at src/tc.rs:230:13:
declaration not found in infer_const, falsePremise
...
error: nanoda exited with 101
```

incomplete でも `declaration not found in infer_const, sorryAx` が確認された。同じ実行では con-leche / con-ron が非標準公理や `sorryAx` を拒否・未対応と記録している。

**判定**：通常の `lake check` による禁止公理の拒否は観測した。一方、nanoda の `panic` は正常な拒否と同一に認定しない。少なくとも独立検査器の**異常終了というソフトウェア品質上の事象**として記録する。ただし、この事象だけで Lean カーネルが不正な証明を受理したとは判断しない。異常終了の設計上の意図や根本原因は別途確認対象である。

## 5. 監査器自身で起きた不具合

初回は単体ケースの一部で証明コードの定義展開不足があり、期待した受理にならなかった。第二次では単体14件が期待どおりになったものの、環境の `bubblewrap` エラーで `lake check` に失敗するケースがあった。第三次ではUbuntu 22.04に移して試験を完了させたが、終了コードだけに依拠する判定器が、上記 `panic` を誤って期待どおりの拒否に分類した。第四次では `panic` を独立判定する修正を入れた。

これは**監査するプログラムも監査対象となる**ことを示す直接の作業記録である。検査器の合格表示を、その表示自身の正当性の無条件の証明として使用しない。

## 6. 正当性に関する工学的判定

### 観測されたこと（E）

- Lean 4.35.0 は上記14ケースで、仕様と入力に応じた受理・拒否を示した。
- 任意公理や `sorry` を用いる証明を受理する場合がある一方、条件を追加した `lake check` はその公理依存を拒否した。
- `--paranoid` は strict で成功し、lax / incomplete では少なくとも一つの独立検査器が異常終了した。
- 初回から第三次の監査過程で、試験プログラム自身の不備も実測によって発覚した。

### 問題提起への判定（I）

**「文字・記号の完全性が保証されないまま形式化し、検査したものを完全な証明と認定できる根拠は何か」という問いに対して、Lean の受理結果や検査器の成功表示そのものは、その根拠にならない。**

Lean が有用な検査操作を実装していることと、そこから「完全な証明」という認定を導く根拠が成立していることを、同じ結論にしない。

### 未観測の事項（U）

- 文字・記号の表現手段そのものの完全性を保証する根拠と検証方法。
- 定義・公理・意味・認定操作に関する全体的な正当化。
- 第四次の `panic` 判別結果（初回保存時点では未完了）。
- 独立検査器の異常終了の原因と修正の要否。

**最終状態：有限な単体検査は PASS、方法論の完全な正当化については根拠未確認、第三次の独立検査器品質には REVIEW_REQUIRED が残る。** この状態を「形式化の完全な正当化が実証された」として閉じない。

---

## 一次資料

- Lean Language Reference — [Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
- Lean Language Reference — [Elaboration and Compilation](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/)
- Lean 4.34.0 — [Release Notes](https://lean-lang.org/doc/reference/latest/releases/v4.34.0/)
- Lean 4.35.0 — [Release Notes](https://lean-lang.org/doc/reference/latest/releases/v4.35.0/)

本記録の版と監査対象の版を混同しない。オンライン最新版の記述は実機 Lean 4.35.0 の実測ログによって確認する。
