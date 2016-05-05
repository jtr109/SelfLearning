(define (square x) (* x x))

(define (sum-of-square x y) (+ (square x) (square y)))

(define (largest-two-sum-square x y z)
        (cond ((= (min x y z) x) (sum-of-square y z))
              ((= (min x y z) y) (sum-of-square x z))
              ((= (min x y z) z) (sum-of-square x y))))

