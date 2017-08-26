; 编写下面的函数。阅读第五节了解如何编写谓词。

; 1. 返回一个实数绝对值的函数。

(define absolute-number
  (lambda (num)
    (if (>= num 0)
      num
      (- 0 num))))

; (define my-abs
;   (lambda (num)
;     (* num
;        (if (positive? num) 1 -1))))

; 2. 返回一个实数的倒数的函数。如果参数为0，则返回#f。

(define reciprocal
  (lambda (num)
    (if (= num 0)
      #f
      (/ 1 num))))

; 3. 将一个整数转化为ASCII码字符的函数。只有在33~126之间的ASCII码才能转换为可见的字符。
; 使用integer->char可以将整数转化为字符。如果给定的整数不能够转化为字符，那么就返回#f。

(define i2a
  (lambda (num)
    (if (<= 33 num 126)
      (integer->char num)
      #f)))
