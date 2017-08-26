; 一个接受三个实数作为参数的函数，若参数皆为正数则返回它们的乘积。

(define positive-product
  (lambda (a b c)
    (if (and (positive? a) (positive? b) (positive? c))
      (* a b c)
      #f)))

; 一个接受三个实数作为参数的函数，若参数至少一个为负数则返回它们的乘积。
(define negative-product
  (lambda (a b c)
    (if (or (negative? a) (negative? b) (negative? c))
      (* a b c)
      #f)))
