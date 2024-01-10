`timescale 1ns/1ps

module Sum_Generator(
    input [127:0] p,
    input [127:0] c,
    output [127:0] Sum
);

    // generate instantiate Sum_Generator for each bit of the vectors
    genvar i;
    generate
        for (i = 0; i < 128; i = i + 1) begin
            xor xor_inst (Sum[i], p[i], c[i]);
        end
    endgenerate 

endmodule
