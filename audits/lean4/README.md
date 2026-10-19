# Lean 4 証明正当性・方法論品質監査（実機検査用）

2026-10-20、Lean 4.35.0を対象とする認知工学の方法論品質検査用資産。
日本語原典・公開正本・旧版は変更しない。HDS内部構造・非公開実装は含めない。

## 最上位の監査要求

文字・記号を用いた形式化において、文字・記号の表現力／意味の完全性そのものが保証されていないとき、形式上の導出成立から、対象についての完全な正当性を導く根拠は何か。

この問いを、形式体系内の「完全性」の特定定義に置換しない。形式的な証明受理は観測対象であって、この問いへの十分な回答ではない。また、製品側が保証境界を明記すること自体は、その保証内容を正当化する根拠にならない。

## ケース

- C01–C08：前回の品質検査に対応した形式受理、誤仕様、公理、sorry、負例の対照。
- C09–C10：同じ文字列「theorem certified : Safety」でも、Safetyの定義を変更すると結果が変わる対照。名前だけで意味を固定できない。
- C11–C12：元の対象の差異を潰す符号化と差異を保持する符号化の対照。
- C13：外部から導入した前提が証明として使われる場合。
- C14：「完全性」という名前を持つ命題の受理と、対象世界についての完全性の間の区別。
- L1–L3：strict／lax／incompleteの3つのLakeプロジェクトのbuild、check、paranoidを個別に記録。

※これは有限の製品試験であって、「言語一般は必ず不完全」という普遍命題をLeanで証明する試験ではない。
※形式受理と表現の正当性・意味対応・公理の正当性を同一視しない。

## 実行、証拠、停止状態

- GitHub Actionsのpushトリガーで監査用ブランチ上で自動実行する。正本mainは変更しない。
- Lean 4.35.0に固定してバージョン、各ケースのstdout/stderr、終了コード、実行時刻、対象コミットを保存する。
- 保存先はActions artifact「lean4-methodology-audit-evidence」内のaudit-output/。
- D＝一次文書、E＝実測、I＝工学的解釈、U＝未観測。期待値をEに昇格させない。
- PASS＝有限な試験条件で期待を満たす。REVIEW_REQUIRED＝試験期待と異なる。FAIL_ENVIRONMENT＝実行できない。普遍的妥当性については別の未観測状態を保持する。

手元での実行例：python3 audits/lean4/run_audit.py --lake

## 一次資料

- https://lean-lang.org/doc/reference/latest/ValidatingProofs/
- https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/
- https://lean-lang.org/doc/reference/latest/releases/v4.34.0/
- https://lean-lang.org/doc/reference/latest/releases/v4.35.0/

オンライン最新版の記述を、4.35.0の実測と無検証で同一視しない。