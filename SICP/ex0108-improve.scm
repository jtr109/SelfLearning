;;; ex0108-improve.scm

(define (improve guess x)
        (/ (+ (/ x
                 (* guess guess))
              (* 2 guess))
           3))

