(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (goodenough? guess x)
  (< (/ (abs (- guess
                (improve guess x)))
        guess)
     (expt 0.1 4)))

(define (sqrt-iter guess x)
  (if (goodenough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(sqrt 2)
(sqrt (* 9 (expt 10 20)))
