`timescale 1ns/1ps

module General_Barrett_Reduction(
    input [63:0] X, // assumption X is a result of integer mulitplication
    input [31:0] q,
    output reg [31:0] r
);

    parameter k = 32; // Adjust the value of k accordingly
    
    reg [31:0] q1, q2, q3;
    reg [31:0] r1, r2, r3;
    reg [31:0] mu;

    // Pre-computation
    // Calculate mu during pre-computation
    always@(*) begin
        mu = (1 << (2 * k)) / q;
    end

    // Step 1: q1 ← ⌊X / 2^k⌋
    always @(*) begin
        q1 = X >> k;    // Step 1: q1 ← ⌊X / 2^k⌋
        q2 = q1 * mu;   // Step 2: q2 ← q1 × mu
        q3 = q2 >> k;   // Step 3: q3 ← ⌊q2 / 2^k⌋
        r1 = (X % (1 << (k + 2))) - (q3 * q % (1 << (k + 2))); // Step 4: r1 ← X mod (2^(k+2)) − (q3 × q) mod (2^(k+2))
        r2 = r1 - q;    // Step 5: r2 ← r1 − q
        r3 = r1 - (q << 1); // Step 6: r3 ← r1 − 2q

        // Step 7: Choose the correct result {r ∈ {r1, r2, r3}|0 ≤ r < q}
        if (r1 >= 0 && r1 < q) begin
            r = r1;
        end else if (r2 >= 0 && r2 < q) begin
            r = r2;
        end else begin
            r = r3;
        end
    end

endmodule