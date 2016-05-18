;;; ex0111-iterative.scm
; a <- b
; b <- c
; c <- a + 2 * b + 3 * c

(define (f-iter a b c counter)
        (if (= counter 0)
            a
            (f-iter b
                    c
                    (+ (* 3 a) (* 2 b) c)
                    (- counter 1))))
(define (f n)
        (f-iter 0 1 2 n))

