;;; ex0107-good-enough.scm

(define (good-enough? old-guess new-guess)
        (< (abs (- old-guess new-guess))
           0.001))

