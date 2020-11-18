void main() {

    struct LIST * SortList1(struct LIST * pList) 
    {
        // Caso a lista seja nula ou não tenha elementos
        if (pList == NULL || pList -> pNext == NULL)
            return pList;
        // head é o primeiro elemento de uma lista ordenada
        struct LIST * head = NULL;
        while (pList != NULL) {
            struct LIST * current = pList;
            pList = pList->pNext;
            if (head == NULL || current->iValue < head->iValue) {
                // Inserção no head da lista ordenada ou
                // como primeiro elemento de uma lsita ordenada vazia
                current->pNext = head;
                head = current;
            } else {
                // Inserção do elemento atual na posição correta de uma lista ordenada populada
                struct LIST * p = head;
                while (p != NULL) {
                    if (p->pNext == NULL || // Último elemento de uma lista ordenada
                        current->iValue < p->pNext->iValue) // Meio da lista
                    {
                        // Inserção no meio da lista ordenada ou como o último elemento
                        current->pNext = p->pNext;
                        p->pNext = current;
                        break; // Fim do laço
                    }
                    p = p->pNext;
                }
            }
        }
        return head;
    }

}
