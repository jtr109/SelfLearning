(load "ex0107-new.scm")

(define (improve-cr x guess)
  (/ (+ (/ x
	   (square guess))
	(* 2 guess))
     3))

(define (cubic-root x guess)
  (if (goodenough? guess x)
     guess
     (cubic-root x
		 (improve-cr x guess))))

(cubic-root 9 1)
