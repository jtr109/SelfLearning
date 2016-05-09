;;; ex0108-cube-iter.scm

(load "ex0107-good-enough.scm")
(load "ex0108-improve.scm")

(define (cube-iter guess x)
        (if (good-enough? guess (improve guess x))
            guess
            (cube-iter (improve guess x)
                       x)))

