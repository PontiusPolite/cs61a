(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond 
    ((< num 0) -1)
    ((= num 0) 0)
    (else 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond 
    ((= y 0) 1)
    ((even? y) 
      (begin 
        (define a (pow x (/ y 2)))
        (* a a)
      )
    )
    (else 
      (begin 
        (define a (pow x (/ (- y 1) 2)))
        (* a a x)
      )
    )
  )
)

